use std::{mem::transmute, sync::{Mutex, OnceLock}};
use minhook::MinHook;
use windows::{core::s, Win32::System::{LibraryLoader::GetModuleHandleA, Memory::{VirtualProtect, PAGE_PROTECTION_FLAGS, PAGE_READWRITE}}};

use crate::dra01::{dll_offsets::Offset, game_data::{Enemy, ObjAttr, OBJ_ATTR_LENGTH}, hooked_functions::{dra_mesg_comm_get_message, es_enemy_dead_sub}};

pub mod hooked_functions;
pub mod game_data;
pub mod dll_offsets;


pub static mut DLL_BASE: usize = 0;

// pointers to the original functions
pub static DRA_MESG_COMM_GET_MESSAGE: OnceLock<extern "system" fn(u32) -> *const u8> = OnceLock::new();
pub static G_WINDOW_SET_MAIN_WINDOW:  OnceLock<extern "system" fn(u32) -> u32>       = OnceLock::new();
pub static ES_ENEMY_DEAD_SUB:         OnceLock<extern "system" fn(*mut u8)>          = OnceLock::new();

// buffer for storing and displaying custom messages 
// todo: does it (still) need mutex?
pub static CUSTOM_MSG: Mutex<[u8; 256]> = Mutex::new([0; 256]);


pub fn hook_functions() {
    unsafe {
        // todo: if dra01 isn't detected, wait and try again
        let dll_base = GetModuleHandleA(s!("dra01.dll")).expect("msg").0 as usize;
        DLL_BASE = dll_base;

        let fn_offset = dll_offset(Offset::GWindowSetMainWindow);
        G_WINDOW_SET_MAIN_WINDOW.set(transmute(fn_offset)).expect("msg");
        //-----
        let fn_offset = dll_offset(Offset::DraMesgCommGetMessage);
        let orig_addr = MinHook::create_hook(fn_offset as _, dra_mesg_comm_get_message as _).expect("create_hook failed");
        DRA_MESG_COMM_GET_MESSAGE.set(transmute(orig_addr)).expect("msg");
        //-----
        let fn_offset = dll_offset(Offset::EsEnemyDeadSub);
        let orig_addr2 = MinHook::create_hook(fn_offset as _, es_enemy_dead_sub as _).expect("create_hook failed");
        ES_ENEMY_DEAD_SUB.set(transmute(orig_addr2)).expect("msg");

        MinHook::enable_all_hooks().expect("failed to enable hooks");
    }
}

// patch dra01.dll in memory (temporary patch until dll unloads)
pub fn patch_dra01() {
    let contents = std::fs::read_to_string("test.txt").expect("msg");
    println!("{}", contents);

    unsafe {
        let obj_attr_ptr = dll_offset(Offset::ObjAttrTable) as *mut ObjAttr;
        let region_size = size_of::<ObjAttr>() * OBJ_ATTR_LENGTH;

        let mut old_protect = PAGE_PROTECTION_FLAGS(0);
        match VirtualProtect(
            obj_attr_ptr as _,
            region_size,
            PAGE_READWRITE,
            &mut old_protect,
        ) {
            Ok(_) => {
                let region = std::slice::from_raw_parts_mut(obj_attr_ptr, 118);
                region[Enemy::FlyingArmor.id()].soul_id = 0x01;

                let mut dummy = PAGE_PROTECTION_FLAGS(0);
                let _ = VirtualProtect(
                    obj_attr_ptr as _,
                    region_size,
                    old_protect,
                    &mut dummy,
                );
            }

            Err(e) => println!("failed to modify game: {}", e),
        }
    }
}

pub fn dll_offset(offset: Offset) -> usize {
    unsafe { DLL_BASE + offset.get() }
}
