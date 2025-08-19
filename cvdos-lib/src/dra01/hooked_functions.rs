use crate::dra01::{dll_offset, dll_offsets::Offset, game_data::{Enemy, MagicCirclePos, ObjAttr, OBJ_ATTR_LENGTH}, BALORE_DEFEAT, CUSTOM_MSG, DLL_BASE, DRA_MESG_COMM_GET_MESSAGE, ENM_SET_FIRST, ES_ENEMY_DEAD_SUB, G_ITEM_SET};

// originally, receiving a soul is what re-opens boss doors.
// this will open the doors if the killed enemy is a boss.
// not an optimal solution since you can miss the item if you leave!
// but it works for now. a proper fix would be to make the item itself open the doors.
pub fn es_enemy_dead_sub(p_obj_data: *mut u8) {
    // let mut old_hard_mode = None;

    unsafe {
        // todo: create an Enemy fn that returns all boss IDs that should open doors
        // actually, not all bosses will call this function!
        if *p_obj_data.add(0x3E8) == Enemy::FlyingArmor.id() {
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag

            // set effective luck really high to guarantee a drop.
            // todo: needs to take hard mode into account
            let effective_luck = (DLL_BASE + 0x964482) as *mut u16;
            effective_luck.write(4095);

            // set flying armor position to the magic circle, to prevent items
            // dropping out of bounds.
            let mc_pos = dll_offset(Offset::MagicCirclePos) as *const MagicCirclePos;
            let p_obj_x = p_obj_data.add(0x2C) as *mut u32;
            let p_obj_y = p_obj_data.add(0x30) as *mut u32;
            p_obj_x.write((*mc_pos).x);
            p_obj_y.write((*mc_pos).y);
        }
    }

    if let Some(orig_fn) = ES_ENEMY_DEAD_SUB.get() {
        orig_fn(p_obj_data);
    }
}

// this function returns a text message based on msg_id. send 0xFFF to
// return CUSTOM_MSG instead, for custom message printing.
pub fn dra_mesg_comm_get_message(msg_id: u32) -> *const u8 {
    if msg_id != 0xFFF && let Some(orig_fn) = DRA_MESG_COMM_GET_MESSAGE.get() {
        orig_fn(msg_id)
    } else {
        CUSTOM_MSG.lock().unwrap().as_ptr()
    }
}

// balore doesn't drop items by default, so call the item drop function here if necessary.
pub fn balore_defeat(p_obj_data: *mut u64, a: u64, b: u64, c:u64) {
    // todo: only do this if balore drops an item!
    unsafe {
        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr[Enemy::Balore.id() as usize].soul_id == 0xFF {
            let p_flags = dll_offset(Offset::FlagsGlobal) as *const u8;
            if *p_flags & 0b1000 == 0 {
                if let Some(orig_fn) = G_ITEM_SET.get() {
                    let pos_x = (8 << 16) as u64;
                    let pos_y = (6 << 16) as u64;
                    let pos = pos_x | (pos_y << 32);
                    orig_fn(&pos, 0xB8, 0);

                    // open boss doors. temp fix! since you can miss the item this way
                    let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
                    *p_flags_global &= 0xFD; // clear boss door flag
                }
            }

            if let Some(orig_fn) = BALORE_DEFEAT.get() {
                let p_game_mode = (DLL_BASE + 0x964346) as *mut u8;
                p_game_mode.write(1);
                orig_fn(p_obj_data, a, b, c);
                p_game_mode.write(0);
            }
        }
    }
}

pub fn enm_set_first(arg1: u64) {
    println!("request id: 0x{:0X}", arg1);

    if let Some(orig_fn) = ENM_SET_FIRST.get() {
        orig_fn(arg1);
    }
}
