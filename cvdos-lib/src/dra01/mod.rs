use std::{ffi::c_void, mem::transmute, slice::from_raw_parts_mut, sync::{Mutex, OnceLock}};
use minhook::MinHook;
use windows::{core::s, Win32::System::{LibraryLoader::GetModuleHandleA, Memory::{VirtualProtect, PAGE_EXECUTE_READWRITE, PAGE_PROTECTION_FLAGS, PAGE_READWRITE}}};

use crate::{dra01::{dll_offsets::Offset, game_data::{Enemy, EnmSetData, ObjAttr, OBJ_ATTR_LENGTH}, hooked_functions::{dra_mesg_comm_get_message, es_enemy_dead_sub}}, handle_command};

pub mod hooked_functions;
pub mod game_data;
pub mod dll_offsets;

const DEBUG: bool = true;

pub static mut DLL_BASE: usize = 0;

// pointers to the original functions
pub static G_WINDOW_SET_MAIN_WINDOW:  OnceLock<extern "system" fn(u32) -> u32>       = OnceLock::new();
pub static GET_ENM_LIST:              OnceLock<extern "system" fn(u64, u64) -> u64>  = OnceLock::new();
pub static ES_ENEMY_DEAD_SUB:         OnceLock<extern "system" fn(*mut u8)>          = OnceLock::new();
pub static DRA_MESG_COMM_GET_MESSAGE: OnceLock<extern "system" fn(u32) -> *const u8> = OnceLock::new();

pub static ENM_SET_FIRST:             OnceLock<extern "system" fn(u64)>  = OnceLock::new();

// buffer for storing and displaying custom messages 
// todo: does it (still) need mutex?
pub static CUSTOM_MSG: Mutex<[u8; 256]> = Mutex::new([0; 256]);


pub fn hook_functions() {
    unsafe {
        // todo: if dra01 isn't detected, wait and try again
        let dll_base = GetModuleHandleA(s!("dra01.dll")).expect("msg").0 as usize;
        DLL_BASE = dll_base;

        // todo: split out unhooked functions to own fn
        let fn_offset = dll_offset(Offset::GWindowSetMainWindow);
        G_WINDOW_SET_MAIN_WINDOW.set(transmute(fn_offset)).expect("msg");
        //-----
        let fn_offset = dll_offset(Offset::GetEnmList);
        GET_ENM_LIST.set(transmute(fn_offset)).expect("msg");

        //-----

        let fn_offset = dll_offset(Offset::DraMesgCommGetMessage);
        let orig_addr = MinHook::create_hook(fn_offset as _, dra_mesg_comm_get_message as _).expect("create_hook failed");
        DRA_MESG_COMM_GET_MESSAGE.set(transmute(orig_addr)).expect("msg");
        //-----
        let fn_offset = dll_offset(Offset::EsEnemyDeadSub);
        let orig_addr2 = MinHook::create_hook(fn_offset as _, es_enemy_dead_sub as _).expect("create_hook failed");
        ES_ENEMY_DEAD_SUB.set(transmute(orig_addr2)).expect("msg");

        if DEBUG {
            let fn_offset = DLL_BASE + 0x03F420;
            let orig_addr = MinHook::create_hook(fn_offset as _, enm_set_first as _).expect("create_hook failed");
            ENM_SET_FIRST.set(transmute(orig_addr)).expect("msg");
        }

        MinHook::enable_all_hooks().expect("failed to enable hooks");
    }
}

fn enm_set_first(arg1: u64) {
    println!("request id: 0x{:0X}", arg1);

    if let Some(orig_fn) = ENM_SET_FIRST.get() {
        orig_fn(arg1);
    }
}

// patch dra01.dll in memory (temporary patch until dll unloads)
pub fn patch_dra01() {
    apply_ap_patch();
    item_vanish_timer();
}

// modifies page protection flags, call obj_attr_restore_protection_flags() to restore
fn obj_attr_get_list() -> (&'static mut [ObjAttr], PAGE_PROTECTION_FLAGS) {
    unsafe {
        let obj_attr_ptr = dll_offset(Offset::ObjAttrTable) as *mut ObjAttr;
        let region_size = size_of::<ObjAttr>() * OBJ_ATTR_LENGTH;

        match virtual_protect(obj_attr_ptr as _, region_size, PAGE_READWRITE) {
            Ok(old_protect) => {
                let region = std::slice::from_raw_parts_mut(obj_attr_ptr, 118);
                // region[Enemy::FlyingArmor.id()].soul_id = 0xFF;
                // region[Enemy::FlyingArmor.id()].item1 = 0x93;
                // region[Enemy::FlyingArmor.id()].item_rarity = 0xFF;

                (region, old_protect)

                // let _ = virtual_protect(obj_attr_ptr as _, region_size, old_protect);
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

fn apply_ap_patch() {
    let data = std::fs::read("AP_28556804547610715814_P1_fred.patch").expect("msg");
    
    let (obj_attr_list, old_protect) = obj_attr_get_list();

    let mut pos = 0;
    while pos < data.len() {
        match data[pos] {
            1 => { // static item location
                let enm_list = get_enm_list(data[pos + 1] as u16);
                let offset = data[pos + 2] as usize;

                match data[pos + 3] {
                    0x11 => { // item
                        let item_offset = match data[pos + 4] {
                            0x01 ..= 0x3D => (2, 1),   // items
                            0x44 ..= 0x90 => (3, 67),  // weapons
                            0x92 ..= 0xCE => (4, 146), // armor / accessories
                            _ => (0xFF, 0),
                        };
                        // todo: either create or call item type to (class, subtype) fn here
                        enm_list[offset].type2 = item_offset.0;
                        enm_list[offset].var2 = (data[pos + 4] - item_offset.1) as u16;
                    }

                    0x12 => { // soul
                        // soul pedestal
                        enm_list[offset].type1 = 2;
                        enm_list[offset].type2 = 1;

                        enm_list[offset].var1 = 0;
                        // soul ID
                        enm_list[offset].var2 = data[pos + 4] as u16;
                    }

                    _ => todo!(),
                }

                pos += 5;
            }
            
            2 => { // boss location
                let offset = data[pos + 1] as usize;

                match data[pos + 2] {
                    0x11 => { // item
                        let offset = data[pos + 1] as usize;
                        // obj_attr_list[offset].soul_id = data[pos + 2];
                        obj_attr_list[offset].soul_id = 0xFF;
                        obj_attr_list[offset].item1 = data[pos + 3] as u16;
                        obj_attr_list[offset].item_rarity = 0xFF;
                    }

                    0x12 => { // soul
                        obj_attr_list[data[pos + 1] as usize].soul_id = data[pos + 3];
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

            // todo: what to do about the length param? could scan for list terminator probably
            let region = std::slice::from_raw_parts_mut(ptr3, 13);
            region
            // soul pedestal
            // region[5].type1 = 4;
            // region[5].type2 = 5;

            // region[5].var1 = 0;
            // soul ID
            // region[5].var2 = 0x08;
        }
    } else {
        todo!()
    }
}
