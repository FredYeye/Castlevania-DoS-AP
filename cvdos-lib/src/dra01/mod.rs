use std::{ffi::c_void, mem::transmute, path::PathBuf, sync::{Mutex, OnceLock}};
use minhook::MinHook;
use windows::{core::s, Win32::System::{LibraryLoader::GetModuleHandleA, Memory::{VirtualProtect, PAGE_EXECUTE_READWRITE, PAGE_PROTECTION_FLAGS, PAGE_READWRITE}}};

use crate::dra01::{dll_offsets::Offset, game_data::{Enemy, EnmSetData, ObjAttr, OBJ_ATTR_LENGTH}, hooked_functions::{abaddon_defeat, balore_defeat, dev_ev_08_00, dra_mesg_comm_get_message, enm_set_first, es_enemy_dead_sub, es_soul_drop, gergoth_defeat, paranoia_defeat}};

pub mod hooked_functions;
pub mod game_data;
pub mod dll_offsets;

const DEBUG: bool = true;

pub static mut DLL_BASE: usize = 0;
pub static mut MINA_DATA: (bool, u8) = (false, 0);

// pointers to the original functions
pub static G_WINDOW_SET_MAIN_WINDOW:  OnceLock<extern "system" fn(u32) -> u32>              = OnceLock::new();
pub static GET_ENM_LIST:              OnceLock<extern "system" fn(u64, u64) -> u64>         = OnceLock::new();
pub static ES_ENEMY_DEAD_SUB:         OnceLock<extern "system" fn(*mut u8)>                 = OnceLock::new();
pub static DRA_MESG_COMM_GET_MESSAGE: OnceLock<extern "system" fn(u32) -> *const u8>        = OnceLock::new();
pub static ENM_SET_FIRST:             OnceLock<extern "system" fn(u64)>                     = OnceLock::new();
pub static BALORE_DEFEAT:             OnceLock<extern "system" fn(*mut u64, u64, u64, u64)> = OnceLock::new();
pub static G_ITEM_SET:                OnceLock<extern "system" fn(*const u64, u32, u32)>    = OnceLock::new();
pub static G_ITEM_ADD_RMK_ITEM_NUM:   OnceLock<extern "system" fn(u32) -> bool>             = OnceLock::new();
pub static DEV_EV_08_00:              OnceLock<extern "system" fn (*const u8)>              = OnceLock::new();
pub static ES_SOUL_DROP:              OnceLock<extern "system" fn(*mut u8, *const u64)>     = OnceLock::new();
pub static GERGOTH_DEFEAT:            OnceLock<extern "system" fn(*mut u8, u64, u64, u64)>  = OnceLock::new();
pub static G_WINDOW_SET_ITEM_NAME:    OnceLock<extern "system" fn(i32, i32)>                = OnceLock::new();
pub static PARANOIA_DEFEAT:           OnceLock<extern "system" fn(*mut u8, u64, u64, u64)>  = OnceLock::new();
pub static ABADDON_DEFEAT:            OnceLock<extern "system" fn(*mut u8, u64, u64, u64)>  = OnceLock::new();

// buffer for storing and displaying custom messages 
// todo: does it (still) need mutex?
pub static CUSTOM_MSG: Mutex<[u8; 256]> = Mutex::new([0; 256]);

pub fn hook_functions() {
    unsafe {
        // todo: if dra01 isn't detected, wait and try again?
        // it seems to be loaded in the intro though... and then reloaded once entering the game

        let dll_base = GetModuleHandleA(s!("dra01.dll")).expect("msg").0 as usize;
        DLL_BASE = dll_base;

        // todo: split out unhooked functions to own fn?
        let fn_offset = dll_offset(Offset::GItemAddRmkItemNum);
        G_ITEM_ADD_RMK_ITEM_NUM.set(transmute(fn_offset)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::GWindowSetMainWindow);
        G_WINDOW_SET_MAIN_WINDOW.set(transmute(fn_offset)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::GetEnmList);
        GET_ENM_LIST.set(transmute(fn_offset)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::GItemSet);
        G_ITEM_SET.set(transmute(fn_offset)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::GWindowSetItemName);
        G_WINDOW_SET_ITEM_NAME.set(transmute(fn_offset)).expect("msg");
        // -----

        let fn_offset = dll_offset(Offset::DraMesgCommGetMessage);
        let orig_addr = MinHook::create_hook(fn_offset as _, dra_mesg_comm_get_message as _).expect("create_hook failed");
        DRA_MESG_COMM_GET_MESSAGE.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::EsEnemyDeadSub);
        let orig_addr = MinHook::create_hook(fn_offset as _, es_enemy_dead_sub as _).expect("create_hook failed");
        ES_ENEMY_DEAD_SUB.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::BaloreDefeat);
        let orig_addr = MinHook::create_hook(fn_offset as _, balore_defeat as _).expect("create_hook failed");
        BALORE_DEFEAT.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::DevEv08_00);
        let orig_addr = MinHook::create_hook(fn_offset as _, dev_ev_08_00 as _).expect("create_hook failed");
        DEV_EV_08_00.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::EsSoulDrop);
        let orig_addr = MinHook::create_hook(fn_offset as _, es_soul_drop as _).expect("create_hook failed");
        ES_SOUL_DROP.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::GergothDefeat);
        let orig_addr = MinHook::create_hook(fn_offset as _, gergoth_defeat as _).expect("create_hook failed");
        GERGOTH_DEFEAT.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::ParanoiaDefeat);
        let orig_addr = MinHook::create_hook(fn_offset as _, paranoia_defeat as _).expect("create_hook failed");
        PARANOIA_DEFEAT.set(transmute(orig_addr)).expect("msg");
        // -----
        let fn_offset = dll_offset(Offset::AbaddonDefeat);
        let orig_addr = MinHook::create_hook(fn_offset as _, abaddon_defeat as _).expect("create_hook failed");
        ABADDON_DEFEAT.set(transmute(orig_addr)).expect("msg");
        // -----

        if DEBUG {
            let fn_offset = DLL_BASE + 0x03F420;
            let orig_addr = MinHook::create_hook(fn_offset as _, enm_set_first as _).expect("create_hook failed");
            ENM_SET_FIRST.set(transmute(orig_addr)).expect("msg");
        }

        MinHook::enable_all_hooks().expect("failed to enable hooks");
    }
}

// patch dra01.dll in memory (temporary patch until dll unloads)
pub fn patch_dra01() {
    if let Some(patch) = find_patch_file() {
        luck_formula();
        apply_ap_patch(&patch);
        item_vanish_timer();
        balore_prevent_block_exit();
        println!("Found and applied patch {:?}", patch);
    } else {
        println!("No *.patch file found, no changes applied.");
    }
}

fn luck_formula() {
    // todo: "shl ax,05" multiplies luck by 32. replace with imul:
    // imul eax,eax,<scaling_val> | imul r32,r32,imm8 (max scaling: 127)
    // where <scaling_val> is an i8 passed into this function.

    // todo: item2

    // change the drop formula to make each point in luck give a linear increase.
    // this makes luck give ~0.1% increase per point in luck.

    // from: (scaled_soul_rarity + 1) / (32768 - scaled_luck)
    // to:   (scaled_soul_rarity + 1 + scaled_luck) / 32768
    let soul_drop_mod = [
        // 14AB2E
        0x66, 0x0F, 0x1F, 0x44, 0x00, 0x00,                         // nop
        0x66, 0x0F, 0x1F, 0x44, 0x00, 0x00,                         // nop
        0x66, 0xC1, 0xE0, 0x05,                                     // shl ax,05
        0x4C, 0x89, 0x6C, 0x24, 0x58,                               // mov [rsp+58],r13
        0xBA, 0x00, 0x80, 0x00, 0x00,                               // mov edx,00008000
        0x0F, 0xBF, 0xE8,                                           // movsx ebp,ax
        0x8B, 0xCA,                                                 // mov ecx,edx
        0x4C, 0x8D, 0x25, 0xAC, 0x54, 0xEB, 0xFF,                   // lea r12,[dra01.dll]
        0x45, 0x0F, 0xBE, 0x8C, 0xFC, 0xD2, 0x55, 0x27, 0x00,       // movsx r9d,byte ptr [r12+rdi*8+002755D2]
        0x33, 0xDB,                                                 // xor ebx,ebx
        0x41, 0xBD, 0x00, 0x10, 0x00, 0x00,                         // mov r13d,00001000
        0x45, 0x84, 0xC9,                                           // test r9b,r9b
        0x0F, 0x88, 0xA5, 0x00, 0x00, 0x00,                         // js dra01.dll+14AC13
        0x41, 0x0F, 0xB6, 0x84, 0xFC, 0xCC, 0x55, 0x27, 0x00,       // movzx eax,byte ptr [r12+rdi*8+002755CC]
        0x84, 0xC0,                                                 // test al,al
        0x74, 0x47,                                                 // je dra01.dll+14ABC2
        0x44, 0x8B, 0xC0,                                           // mov r8d,eax
        0x41, 0xC1, 0xE0, 0x06,                                     // shl r8d,06
        0x66, 0x83, 0x3D, 0x96, 0x99, 0x81, 0x00, 0x38,             // cmp word ptr [dra01.dll+964520],38
        0x75, 0x08,                                                 // jne dra01.dll+14AB97
        0x46, 0x8D, 0x04, 0x45, 0x08, 0x00, 0x00, 0x00,             // lea r8d,[r8*2+00000008]
        0xF7, 0x05, 0x36, 0x93, 0x81, 0x00, 0x00, 0x00, 0x00, 0x10, // test [dra01.dll+963ED4],10000000
        0x44, 0x0F, 0x45, 0xC2,                                     // cmovne r8d,edx
        0x41, 0x01, 0xE8,                                           // add r8d,ebp
        0xE8, 0xF6, 0xED, 0xEC, 0xFF,                               // call dra01.dll+199A0
        0x41, 0x3B, 0xC0,                                           // cmp eax,r8d
    ];

    // from: scaled_item_rarity / (8192 - scaled_luck)
    // to:   (scaled_item_rarity + scaled_luck) / 8192
    let item1_drop_mod = [
        // 14ACFF
        0x44, 0x89, 0xD1,                                           // mov ecx,r10d
        0xE8, 0x99, 0xEC, 0xEC, 0xFF,                               // call getRandF
        0x8B, 0x0D, 0x51, 0x5F, 0xA3, 0x00,                         // mov ecx,dword ptr [dra01.dll+8EB244]
        0xC1, 0xEA, 0x02,                                           // shr edx,0x2 +1
        0x41, 0x01, 0xD0,                                           // add r8d,edx 
        0x66, 0x0F, 0x1F, 0x84, 0x00, 0x00, 0x00, 0x00, 0x00,       // nop
        0x66, 0x2E, 0x0F, 0x1F, 0x84, 0x00, 0x00, 0x00, 0x00, 0x00, // nop
        0x66, 0x2E, 0x0F, 0x1F, 0x84, 0x00, 0x00, 0x00, 0x00, 0x00, // nop
        0x44, 0x39, 0xC0,                                           // cmp ebx,r8d
    ];

    unsafe {
        let code_loc = (DLL_BASE + 0x14AB2E) as *mut u8;
        let region_size = 0x14AD33 - 0x14AB2E;

        match virtual_protect(code_loc as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                let region = std::slice::from_raw_parts_mut(code_loc, region_size);

                region[0 .. soul_drop_mod.len()].copy_from_slice(&soul_drop_mod);

                region[0x17A .. 0x17A + 3].copy_from_slice(&[0x89, 0xEA, 0x90]); // mov edx,ebp + nop 
                region[0x1D1 .. 0x1D1 + item1_drop_mod.len()].copy_from_slice(&item1_drop_mod);

                let _ = virtual_protect(code_loc as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

// modifies page protection flags, call obj_attr_restore_protection_flags() to restore
fn obj_attr_get_list() -> (&'static mut [ObjAttr], PAGE_PROTECTION_FLAGS) {
    unsafe {
        let obj_attr_ptr = dll_offset(Offset::ObjAttrTable) as *mut ObjAttr;
        let region_size = size_of::<ObjAttr>() * OBJ_ATTR_LENGTH;

        match virtual_protect(obj_attr_ptr as _, region_size, PAGE_READWRITE) {
            Ok(old_protect) => {
                let region = std::slice::from_raw_parts_mut(obj_attr_ptr, 118);
                (region, old_protect)
            }

            Err(e) => todo!("failed to modify game: {}", e),
        }
    }
}

fn obj_attr_restore_protection_flags(old_protect: PAGE_PROTECTION_FLAGS) {
    let obj_attr_ptr = dll_offset(Offset::ObjAttrTable) as *mut ObjAttr;
    let region_size = size_of::<ObjAttr>() * OBJ_ATTR_LENGTH;
    let _ = virtual_protect(obj_attr_ptr as _, region_size, old_protect);
}

fn find_patch_file() -> Option<PathBuf> {
    let current_dir = std::env::current_dir().expect("Error accessing current directory");
    for entry in std::fs::read_dir(&current_dir).expect("Error reading current directory") {
        if let Ok(entry) = entry {
            if entry.path().extension().and_then(|ext| ext.to_str()) == Some("patch") {
                return Some(entry.path());
            }
        }
    }

    None
}

fn apply_ap_patch(path: &PathBuf) {
    let data = std::fs::read(path).expect("msg");

    let (obj_attr_list, old_protect) = obj_attr_get_list();

    let mut pos = 0;
    while pos < data.len() {
        match data[pos] {
            1 => { // static item location
                let map_id = u16::from_le_bytes([data[pos + 1], data[pos + 2]]);
                let enm_list = get_enm_list(map_id);
                let offset = data[pos + 3] as usize;
                
                if map_id == 0x54 { // mina's talisman event
                    minas_talisman_event_item(data[pos + 4], data[pos + 5]);
                    pos += 6;
                    continue;
                }

                match data[pos + 4] {
                    0x11 => { // item
                        // if replacing a soul pedestal, add a pickup flag.
                        if enm_list[offset].type1 == 2 && enm_list[offset].type2 == 1 {
                            if map_id == 0xA6 { // doppelganger pedestal
                                enm_list[offset].var1 = 0x80;
                            } else if map_id == 0x164 { // hippogryph pedestal
                                enm_list[offset].var1 = 0x81;
                            }
                        }

                        let item_offset = match data[pos + 5] {
                            0x01 ..= 0x42 => (2, 1),   // items
                            0x44 ..= 0x90 => (3, 67),  // weapons
                            0x92 ..= 0xCE => (4, 146), // armor / accessories
                            _ => (0xFF, 0),
                        };

                        enm_list[offset].type1 = 4;
                        enm_list[offset].type2 = item_offset.0;
                        enm_list[offset].var2 = (data[pos + 5] - item_offset.1) as u16;
                    }

                    0x12 => { // soul
                        // soul pedestal
                        enm_list[offset].type1 = 2;
                        enm_list[offset].type2 = 1;

                        enm_list[offset].var1 = 0;
                        // soul ID
                        enm_list[offset].var2 = data[pos + 5] as u16;
                    }

                    _ => todo!(),
                }

                pos += 6;
            }
            
            2 => { // boss location
                let enm_id = data[pos + 1] as usize;

                match data[pos + 2] {
                    0x11 => { // item
                        obj_attr_list[enm_id].soul_id = 0xFF;
                        obj_attr_list[enm_id].item1 = data[pos + 3] as u16;
                        obj_attr_list[enm_id].item_rarity = 0xFF;
                    }

                    0x12 => { // soul
                        obj_attr_list[enm_id].soul_id = data[pos + 3];

                        // some bosses have hardcoded soul drops, so modify here
                        // todo: needed for more bosses...
                        if enm_id as u8 == Enemy::Balore.id() {
                            balore_custom_soul_drop(data[pos + 3]);
                        } else if enm_id as u8 == Enemy::Paranoia.id() {
                            paranoia_custom_soul_drop(data[pos + 3]);
                        } else if enm_id as u8 == Enemy::Abaddon.id() {
                            abaddon_custom_soul_drop(data[pos + 3]);
                        }
                    }

                    _ => todo!(),
                }

                pos += 4;
            }
            _ => todo!(),
        }
    }

    obj_attr_restore_protection_flags(old_protect);
}

// todo: consolidate *_custom_soul_drop functions
fn balore_custom_soul_drop(soul_id: u8) {
    unsafe {
        let code_loc = (DLL_BASE + 0x1365DB) as *mut u8;
        let region_size = 1;

        match virtual_protect(code_loc as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                code_loc.write(soul_id);

                let _ = virtual_protect(code_loc as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

fn paranoia_custom_soul_drop(soul_id: u8) {
    unsafe {
        let code_loc = (DLL_BASE + 0x12DA13) as *mut u8;
        let region_size = 1;

        match virtual_protect(code_loc as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                code_loc.write(soul_id);

                let _ = virtual_protect(code_loc as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

fn abaddon_custom_soul_drop(soul_id: u8) {
    unsafe {
        let code_loc = (DLL_BASE + 0x18134B) as *mut u8;
        let region_size = 1;

        match virtual_protect(code_loc as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                code_loc.write(soul_id);

                let _ = virtual_protect(code_loc as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

// modifications to the function DevEv08_00 to make Arikado give you a custom item
fn minas_talisman_event_item(item_or_soul: u8, item_id: u8) {
    unsafe {
        let code_loc = (DLL_BASE + 0x1ECBA1) as *mut u8;
        let region_size = 14;

        match virtual_protect(code_loc as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                let region = std::slice::from_raw_parts_mut(code_loc, region_size);

                // 6-byte nop: overwrite mov that adds mina's talisman
                region[0 .. 6].copy_from_slice(&[0x66, 0x0F, 0x1F, 0x44, 0x00, 0x00]);

                let mut message = item_id as u16 - 1;

                MINA_DATA.1 = item_id;

                if item_or_soul == 0x12 {
                    message += 0x289;
                    MINA_DATA.0 = true;
                } else {
                    MINA_DATA.0 = false;
                }

                // update the item window message ID to match the item received
                region[0x0C .. 0x0C + 2].copy_from_slice(&message.to_le_bytes());

                let _ = virtual_protect(code_loc as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

fn item_vanish_timer() {
    unsafe {
        let item_vanish_timer = (DLL_BASE + 0x046098) as *mut u32;
        let region_size = size_of::<u32>();

        match virtual_protect(item_vanish_timer as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                // original instruction: B8 2C 01 00 00 | MOV EAX,0x12C
                *item_vanish_timer = 0x000BB8B8;

                let _ = virtual_protect(item_vanish_timer as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

fn balore_prevent_block_exit() {
    unsafe {
        let blocks_row_count = (DLL_BASE + 0x137944) as *mut u8;
        let region_size = size_of::<u8>();

        match virtual_protect(blocks_row_count as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                // original instruction: 41 bc>10<00 00 00 | MOV R12D,0x10
                *blocks_row_count = 7;

                let _ = virtual_protect(blocks_row_count as _, region_size, old_protect);
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

pub fn dll_offset(offset: Offset) -> usize {
    unsafe { DLL_BASE + offset.get() }
}

fn virtual_protect(ptr: *const c_void, len: usize, protect: PAGE_PROTECTION_FLAGS) -> Result<PAGE_PROTECTION_FLAGS, windows::core::Error> {
    unsafe {
        let mut old_protect = PAGE_PROTECTION_FLAGS(0);
        match VirtualProtect(
            ptr,
            len,
            protect,
            &mut old_protect,
        ) {
            Ok(_) => Ok(old_protect),
            Err(e) => Err(e),
        }
    }
}

fn get_enm_list(map_id: u16) -> &'static mut [EnmSetData] {
    let request = 0x0001000011000000 | ((map_id as u64) << 32);

    if let Some(orig_fn) = GET_ENM_LIST.get() {
        unsafe {
            let ptr1 = dll_offset(Offset::DataPtr) as *const u64;
            let ptr2 = *ptr1 + 0x490; // 0x490 = enm_set_data
            let ptr3 = orig_fn(ptr2, request) as *mut EnmSetData;

            // todo: what to do about the length param? could scan for list terminator if necessary
            let region = std::slice::from_raw_parts_mut(ptr3, 13);
            region
        }
    } else {
        todo!()
    }
}

fn add_soul(soul_id: u8) {
    let offset = (soul_id >> 1) as usize;

    unsafe {
        let ptr = dll_offset(Offset::InventorySouls) as *mut u8;
        let region = std::slice::from_raw_parts_mut(ptr, 0x3E);

        let shift_count = ((soul_id & 1)) * 4;
        if (region[offset] >> shift_count) & 0b1111 < 9 {
            region[offset] += 1 << shift_count;
        }
    }
}
