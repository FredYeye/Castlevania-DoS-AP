use std::{ffi::c_void, mem::transmute, sync::{Mutex, OnceLock}};
use minhook::MinHook;
use windows::{core::s, Win32::System::{LibraryLoader::GetModuleHandleA, Memory::{VirtualProtect, PAGE_EXECUTE_READWRITE, PAGE_PROTECTION_FLAGS}}};

use crate::dra01::{dll_offsets::Offset, game_data::{Enemy, EnmSetData, ObjAttr, OBJ_ATTR_LENGTH}, hooked_functions::{dra_mesg_comm_get_message, es_enemy_dead_sub}};

pub mod hooked_functions;
pub mod game_data;
pub mod dll_offsets;


pub static mut DLL_BASE: usize = 0;

// pointers to the original functions
pub static DRA_MESG_COMM_GET_MESSAGE: OnceLock<extern "system" fn(u32) -> *const u8> = OnceLock::new();
pub static G_WINDOW_SET_MAIN_WINDOW:  OnceLock<extern "system" fn(u32) -> u32>       = OnceLock::new();
pub static ES_ENEMY_DEAD_SUB:         OnceLock<extern "system" fn(*mut u8)>          = OnceLock::new();

pub static GET_ENM_LIST:              OnceLock<extern "system" fn(u64, u64) -> u64>  = OnceLock::new();

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
        let fn_offset = DLL_BASE + 0x14660;
        GET_ENM_LIST.set(transmute(fn_offset)).expect("msg");

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
    // let contents = std::fs::read_to_string("test.txt").expect("msg");
    // println!("{}", contents);

    item_vanish_timer();
    get_enm_list();

    unsafe {
        let obj_attr_ptr = dll_offset(Offset::ObjAttrTable) as *mut ObjAttr;
        let region_size = size_of::<ObjAttr>() * OBJ_ATTR_LENGTH;

        match virtual_protect(obj_attr_ptr as _, region_size, PAGE_EXECUTE_READWRITE) {
            Ok(old_protect) => {
                let region = std::slice::from_raw_parts_mut(obj_attr_ptr, 118);
                region[Enemy::FlyingArmor.id()].soul_id = 0xFF;
                region[Enemy::FlyingArmor.id()].item1 = 0x93;
                region[Enemy::FlyingArmor.id()].item_rarity = 0xFF;

                let _ = virtual_protect(obj_attr_ptr as _, region_size, old_protect);
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

fn get_enm_list() {
    //todo: take a... room id and region id and construct the second param?

    if let Some(orig_fn) = GET_ENM_LIST.get() {
        unsafe {
            let ptr1 = dll_offset(Offset::DataPtr) as *const u64;
            let ptr2 = *ptr1 + 0x490; // 0x490 = enm_set_data
            let ptr3 = orig_fn(ptr2, 0x0001000F11000000) as *mut EnmSetData;

            // test: modify short sword to something else
            let region = std::slice::from_raw_parts_mut(ptr3, 13);
            region[5].var1 = 0x41;
        }
    }
}
