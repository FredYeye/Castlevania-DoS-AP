use std::{fs::File, io::{stdin, BufRead}, os::windows::io::FromRawHandle, sync::OnceLock, thread};

use tokio::sync::mpsc::{self, Sender};
use tokio_tungstenite::tungstenite::Message;
use windows::Win32::{
    Foundation::*,
    System::{Console::{AllocConsole, GetStdHandle, STD_OUTPUT_HANDLE}, SystemServices::*},
};

use crate::{
    archipelago_rs::{client::ArchipelagoClient, protocol::GameData},
    dra01::{dll_offset, dll_offsets::Offset, hook_functions, hooked_functions::dra_mesg_comm_get_message, patch_dra01, CUSTOM_MSG, DLL_BASE, G_WINDOW_SET_MAIN_WINDOW},
};

mod archipelago_rs;
mod dra01;

static mut STDOUT_FILE: Option<File> = None;

static TX: OnceLock<Sender<Vec<u8>>> = OnceLock::new();

#[unsafe(no_mangle)]
extern "system" fn DllMain(_dll_module: HINSTANCE, call_reason: u32, _: *mut ()) -> bool {
    match call_reason {
        DLL_PROCESS_ATTACH => {
            unsafe {
                // enable console for debugging
                if AllocConsole().is_ok() {
                    if let Ok(std_handle) = GetStdHandle(STD_OUTPUT_HANDLE) {
                        STDOUT_FILE = Some(File::from_raw_handle(std_handle.0 as *mut _));
                    }
                }
            }

            thread::spawn(|| {
                let rt = tokio::runtime::Runtime::new().unwrap();
                rt.block_on(websocket());
            });
        }

        _ => ()
    }

    true
}

// todo: rename function lol
async fn websocket() {
    hook_functions();
    patch_dra01();

    let (tx, mut rx) = mpsc::channel::<Vec<u8>>(128);
    TX.set(tx.clone()).expect("msg");

    println!("Enter the AP server to connect to:");
    let server = stdin().lock().lines().next().unwrap().expect("Failed to read server name");

    println!("Enter slot (player) name:");
    let slot = stdin().lock().lines().next().unwrap().expect("Failed to slot name");

    let mut client = ArchipelagoClient::new(&server).await.expect("Failed to establish connection");
    let game = "Super Metroid";
    client
        .connect(&game, &slot, None, Some(7), vec!["AP".to_string()])
        .await.expect("Failed to connect");

    let (sender, mut receiver) = client.split();

    // listen for AP packets
    let receiver_task = tokio::spawn(async move {
        while let Ok(opt_msg) = receiver.recv().await && let Some(msg) = opt_msg {
            println!("recv'd packet: {:?}\n", msg);

            match msg {
                // ServerMessage::RoomInfo(room_info) => todo!(),
                // ServerMessage::ConnectionRefused(connection_refused) => todo!(),
                // ServerMessage::Connected(connected) => todo!(),
                // ServerMessage::ReceivedItems(received_items) => todo!(),
                // ServerMessage::LocationInfo(location_info) => todo!(),
                // ServerMessage::RoomUpdate(room_update) => todo!(),
                // ServerMessage::Print(print) => todo!(),
                // ServerMessage::PrintJSON(print_json) => todo!(),
                // ServerMessage::DataPackage(data_package) => todo!(),
                // ServerMessage::Bounced(bounced) => todo!(),
                // ServerMessage::InvalidPacket(invalid_packet) => todo!(),
                // ServerMessage::Retrieved(retrieved) => todo!(),
                // ServerMessage::SetReply(set_reply) => todo!(),
                _ => (),
            }
        }
    });

    let sender_task = tokio::spawn(async move {
        loop {

        }

        // todo: send data to AP here
    });

    tokio::select! {
        _ = receiver_task => println!("Reader exited"),
        _ = sender_task => println!("Writer exited"),
    }
}

fn handle_command(data: &[u8]) {
    match data[0] {
        1 => { // receive item
            if data.len() >= 2 {
                if data[1] > 0 {
                    let item_offset = match data[1] {
                        0x01 ..= 0x3D => (0, -1),      // items
                        0x44 ..= 0x90 => (0x24, -67),  // weapons
                        0x92 ..= 0xCE => (0x4C, -146), // armor / accessories
                        _ => (0xFF, 0),
                    };

                    let asd = (data[1] as i32 + item_offset.1) as u8;
                    let offset = (asd >> 1) as usize;

                    unsafe {
                        let ptr = dll_offset(Offset::InventoryItems) as *mut u8;
                        // length is longer than it has to be here but w/e
                        let region = std::slice::from_raw_parts_mut(ptr, 0x6E);

                        let shift_count = ((asd & 1)) * 4;
                        if (region[item_offset.0 + offset] >> shift_count) & 0b1111 < 9 {
                            region[item_offset.0 + offset] += 1 << shift_count;
                        }
                    }

                    received_message(data[1] as u32 + 0x0B);
                }
            }
        }

        2 => { // receive soul
            if data.len() >= 2 {
                let offset = (data[1] >> 1) as usize;

                unsafe {
                    let ptr = dll_offset(Offset::InventorySouls) as *mut u8;
                    let region = std::slice::from_raw_parts_mut(ptr, 0x3E);

                    let shift_count = ((data[1] & 1)) * 4;
                    if (region[offset] >> shift_count) & 0b1111 < 9 {
                        region[offset] += 1 << shift_count;
                    }
                }

                received_message(data[1] as u32 + 0x0294);
            }
        }

        3 => { // receive magic seal
            if data.len() >= 2 {
                if data[1] < 5 {
                    unsafe {
                        let ptr = dll_offset(Offset::InventoryMagicSeals) as *mut u8;
                        *ptr |= 1 << data[1];
                    }

                    received_message(data[1] as u32 + 0x49);
                }
            }
        }

        4 => { // print message
            if data.len() >= 3 {
                let msg_id = u16::from_le_bytes([data[1], data[2]]);

                if let Some(orig_fn) = G_WINDOW_SET_MAIN_WINDOW.get() {
                    orig_fn(msg_id as u32);
                }
            }
        }

        _ => (),
    }
}

fn received_message(msg_id: u32) {
    let mut buf = CUSTOM_MSG.lock().unwrap();
    let msg_item_received = translate_string("Received ");
    buf[.. msg_item_received.len()].copy_from_slice(&msg_item_received);

    let msg_offset = dra_mesg_comm_get_message(msg_id);
    let region = unsafe { std::slice::from_raw_parts(msg_offset, 128) };
    if region[..2] == [0x01, 0x00] && let Some(offset) = region.windows(2).position(|w| w == [0xEA, 0x00]) {
        buf[msg_item_received.len() - 2 .. msg_item_received.len() - 2 + offset + 2 - 2].copy_from_slice(&region[2 .. offset + 2]);
    }

    if let Some(orig_fn) = G_WINDOW_SET_MAIN_WINDOW.get() {
        orig_fn(0xFFF);
    }
}

fn translate_string(input: &str) -> Vec<u8> {
    let mut bytes = vec![0x01, 0x00];

    for ch in input.chars() {
        bytes.push( match ch {
            ' ' => 0x00,

            '&' => 0x06,
            '\'' => 0x07,
            '(' => 0x08,
            ')' => 0x09,
            '*' => 0x0A,
            '+' => 0x0B,
            ',' => 0x0C,
            '-' => 0x0D,
            '.' => 0x0E,
            '/' => 0x0F,
            '0'..='9' => (ch as u8 - b'0') + 0x10,
            ':' => 0x1A,
            ';' => 0x1B,
            '<' => 0x1C,
            '=' => 0x1D,
            '>' => 0x1E,
            '?' => 0x1F,
            '@' => 0x20,
            'A'..='Z' => (ch as u8 - b'A') + 0x21,
            '[' => 0x3B,
            '\\' => 0x3C,
            ']' => 0x3D,
            
            'a'..='z' => (ch as u8 - b'a') + 0x41,
            '{' => 0x5B,

            '\n' => 0xE6,

            _ => todo!("unknown char"),
        });

        bytes.push(0);
    }

    bytes.extend_from_slice(&[0xEA, 0x00]);
    bytes
}
