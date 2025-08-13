use crate::dra01::{dll_offset, dll_offsets::Offset, game_data::Enemy, CUSTOM_MSG, DRA_MESG_COMM_GET_MESSAGE, ES_ENEMY_DEAD_SUB};

// originally, receiving a soul is what re-opens boss doors.
// this will open the doors if the killed enemy is a boss.
// not an optimal solution since you can miss the item if you leave!
// but it works for now. a proper fix would be to make the item itself open the doors.
pub fn es_enemy_dead_sub(p_obj_data: *mut u8) {
    let mut old_hard_mode = None;

    unsafe {
        // todo: create an Enemy fn that returns all boss IDs that should open doors
        if *p_obj_data.add(0x3E8) == Enemy::FlyingArmor.id() as u8 {
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag

            // toggle hard mode to guarantee drops from the boss.
            // maybe just put effective luck really high? i guess it
            // reverts itself the next frame...
            let p_hard_mode = dll_offset(Offset::HardMode) as *mut u8;
            old_hard_mode = Some(*p_hard_mode);
            *p_hard_mode = 1;
        }
    }

    if let Some(orig_fn) = ES_ENEMY_DEAD_SUB.get() {
        orig_fn(p_obj_data);
    }

    // restore the difficulty setting
    if let Some(original_hard_mode) = old_hard_mode {
        let p_hard_mode = dll_offset(Offset::HardMode) as *mut u8;
        unsafe { *p_hard_mode = original_hard_mode; }
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
