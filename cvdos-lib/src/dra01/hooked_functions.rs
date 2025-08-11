use crate::dra01::{dll_offset, dll_offsets::Offset, game_data::Enemy, CUSTOM_MSG, DLL_BASE, DRA_MESG_COMM_GET_MESSAGE, ES_ENEMY_DEAD_SUB};

// originally, receiving a soul is what re-opens boss doors.
// this will open the doors if the killed enemy is a boss.
pub fn es_enemy_dead_sub(p_obj_data: *mut u8) {
    unsafe {
        // todo: create an Enemy fn that returns all boss IDs that should open doors
        if *p_obj_data.add(0x3E8) == Enemy::FlyingArmor.id() as u8 {
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag
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
