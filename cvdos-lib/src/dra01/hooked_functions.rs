use crate::dra01::{add_soul, dll_offset, dll_offsets::Offset, game_data::{Enemy, ObjAttr}, ABADDON_DEFEAT, BALORE_DEFEAT, CUSTOM_MSG, DEV_EV_08_00, DLL_BASE, DRA_MESG_COMM_GET_MESSAGE, ENM_SET_FIRST, ES_ENEMY_DEAD_SUB, ES_SOUL_DROP, GERGOTH_DEFEAT, G_ITEM_ADD_RMK_ITEM_NUM, G_ITEM_SET, G_WINDOW_SET_ITEM_NAME, MINA_DATA, PARANOIA_DEFEAT};

// originally, receiving a soul is what re-opens boss doors.
// this will open the doors if the killed enemy is a boss.
// not an optimal solution since you can miss the item if you leave!
// but it works for now. a proper fix would be to make the item itself open the doors.
pub fn es_enemy_dead_sub(p_obj_data: *mut u8) {
    unsafe {
        // todo: create an Enemy fn that returns all boss IDs that should open doors
        // actually, not all bosses will call this function!
        let enemy_id = *p_obj_data.add(0x3E8);
        if enemy_id == Enemy::FlyingArmor.id() || enemy_id == Enemy::Zephyr.id() || enemy_id == Enemy::Death.id() {
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag

            // set effective luck really high to guarantee a drop.
            // maybe just use gItemSet instead?
            // todo: death dropped coins! switch to gitemset!
            // this might be because of the terrible drop formula. try fixing it first
            let effective_luck = (DLL_BASE + 0x964482) as *mut u16;
            effective_luck.write(1024);

            // set flying armor's position to the middle of the room, to prevent his item
            // dropping out of bounds.
            // todo: this also gets applied to the bosses atm, which isn't necessary but is ok
            let p_obj_x = p_obj_data.add(0x2C) as *mut u32;
            let p_obj_y = p_obj_data.add(0x30) as *mut u32;
            p_obj_x.write(0x0010_0000);
            p_obj_y.write(0x0005_0000);

            

            // let pos_x = (16 << 16) as u64;
            // let pos_y = (5 << 16) as u64;
            // let pos = pos_x | (pos_y << 32);

            // let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
            // let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);
            // let item = obj_attr[enemy_id as usize].item1;

            // if let Some(orig_fn) = G_ITEM_SET.get() {
            //     orig_fn(&pos, item as u32, 0);
            // }
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
    unsafe {
        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr[Enemy::Balore.id() as usize].soul_id == 0xFF {
            let p_flags = dll_offset(Offset::FlagsGlobal) as *const u8;
            if *p_flags & 0b1000 == 0 {
                let pos_x = (8 << 16) as u64;
                let pos_y = (6 << 16) as u64;
                let pos = pos_x | (pos_y << 32);

                let item = obj_attr[Enemy::Balore.id() as usize].item1;

                if let Some(orig_fn) = G_ITEM_SET.get() {
                    orig_fn(&pos, item as u32, 0);
                }

                // open boss doors. temp fix! since you can miss the item this way
                let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
                *p_flags_global &= 0xFD; // clear boss door flag
            }

            if let Some(orig_fn) = BALORE_DEFEAT.get() {
                let p_game_mode = (DLL_BASE + 0x964346) as *mut u8;
                p_game_mode.write(1);
                orig_fn(p_obj_data, a, b, c);
                p_game_mode.write(0);
            }
        } else {
            if let Some(orig_fn) = BALORE_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
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

// mina's talisman event function
pub fn dev_ev_08_00(a: *const u8) {
    unsafe {
        let state_before = a.add(0x0E).read();
        
        if let Some(orig_fn) = DEV_EV_08_00.get() {
            orig_fn(a);
        }
        
        let state_after = a.add(0x0E).read();

        // receiving item from arikado
        if state_before == 0 && state_after == 1 {
            if MINA_DATA.0 {
                add_soul(MINA_DATA.1);
            } else {
                if let Some(orig_fn) = G_ITEM_ADD_RMK_ITEM_NUM.get() {
                    let _ = orig_fn(MINA_DATA.1 as u32);
                }
            }
        }
    }
}

pub fn es_soul_drop(p_obj_data: *mut u8, a: *const u64) {
    unsafe {
        let obj_attr_id = p_obj_data.add(0x3E8).read();

        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr_id == Enemy::PuppetMaster.id() && obj_attr[Enemy::PuppetMaster.id() as usize].soul_id == 0xFF {
            let item = obj_attr[Enemy::PuppetMaster.id() as usize].item1;

            if let Some(orig_fn) = G_ITEM_SET.get() {
                orig_fn(a, item as u32, 0);
            }

            // open boss doors. temp fix! since you can miss the item this way
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag
        } else if obj_attr_id == Enemy::Rahab.id() && obj_attr[Enemy::Rahab.id() as usize].soul_id == 0xFF {
            // rahab's item would be unreachable without the rahab soul.
            // therefore, add the item directly to the inventory instead of dropping it.
            // todo: would be a neat detail to also play the "pickup item" sfx
            let item = obj_attr[Enemy::Rahab.id() as usize].item1;

            if let Some(orig_fn) = G_ITEM_ADD_RMK_ITEM_NUM.get() {
                let _ = orig_fn(item as u32);
            }

            if let Some(orig_fn) = G_WINDOW_SET_ITEM_NAME.get() {
                orig_fn(0, item as i32 - 1);
            }

            // open boss doors
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag
        } else if obj_attr_id == Enemy::Aguni.id() && obj_attr[Enemy::Aguni.id() as usize].soul_id == 0xFF {
            let item = obj_attr[Enemy::Aguni.id() as usize].item1;

            if let Some(orig_fn) = G_ITEM_SET.get() {
                orig_fn(a, item as u32, 0);
            }

            // open boss doors. temp fix! since you can miss the item this way
            let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
            *p_flags_global &= 0xFD; // clear boss door flag
        } else {
            if let Some(orig_fn) = ES_SOUL_DROP.get() {
                orig_fn(p_obj_data, a);
            }
        }
    }
}

// gergoth doesn't drop items by default, so call the item drop function here if necessary.
pub fn gergoth_defeat(p_obj_data: *mut u8, a: u64, b: u64, c:u64) {
    unsafe {
        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr[Enemy::Gergoth.id() as usize].soul_id == 0xFF {
            let p_flags = dll_offset(Offset::FlagsGlobal) as *const u8;
            if *p_flags & 0b1000 == 0 {
                let pos_x = (8 << 16) as u64;
                let pos_y = (174 << 16) as u64;
                let pos = pos_x | (pos_y << 32);

                let item = obj_attr[Enemy::Gergoth.id() as usize].item1;

                if let Some(orig_fn) = G_ITEM_SET.get() {
                    orig_fn(&pos, item as u32, 0);
                }

                // open boss doors. temp fix! since you can miss the item this way
                let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
                *p_flags_global &= 0xFD; // clear boss door flag
            }

            let p_game_mode = (DLL_BASE + 0x964346) as *mut u8;
            p_game_mode.write(1);

            if let Some(orig_fn) = GERGOTH_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }

            p_game_mode.write(0);
        } else {
            if let Some(orig_fn) = GERGOTH_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }
        }
    }
}

// paranoia doesn't drop items by default, so call the item drop function here if necessary.
pub fn paranoia_defeat(p_obj_data: *mut u8, a: u64, b: u64, c:u64) {
    unsafe {
        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr[Enemy::Paranoia.id() as usize].soul_id == 0xFF {
            let p_flags = dll_offset(Offset::FlagsGlobal) as *const u8;
            if *p_flags & 0b1000 == 0 {
                let pos_x = (6 << 16) as u64;
                let pos_y = (6 << 16) as u64;
                let pos = pos_x | (pos_y << 32);

                let item = obj_attr[Enemy::Paranoia.id() as usize].item1;

                if let Some(orig_fn) = G_ITEM_SET.get() {
                    orig_fn(&pos, item as u32, 0);
                }

                // open boss doors. temp fix! since you can miss the item this way
                let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
                *p_flags_global &= 0xFD; // clear boss door flag
            }

            let p_game_mode = (DLL_BASE + 0x964346) as *mut u8;
            p_game_mode.write(1);

            if let Some(orig_fn) = PARANOIA_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }

            p_game_mode.write(0);
        } else {
            if let Some(orig_fn) = PARANOIA_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }
        }
    }
}

// abaddon doesn't drop items by default, so call the item drop function here if necessary.
pub fn abaddon_defeat(p_obj_data: *mut u8, a: u64, b: u64, c:u64) {
    unsafe {
        let p_obj_attr = dll_offset(Offset::ObjAttrTable) as *const ObjAttr;
        let obj_attr = std::slice::from_raw_parts(p_obj_attr, 118);

        if obj_attr[Enemy::Abaddon.id() as usize].soul_id == 0xFF {
            let p_flags = dll_offset(Offset::FlagsGlobal) as *const u8;
            if *p_flags & 0b1000 == 0 {
                let pos_x = (6 << 16) as u64;
                let pos_y = (6 << 16) as u64;
                let pos = pos_x | (pos_y << 32);

                let item = obj_attr[Enemy::Abaddon.id() as usize].item1;

                if let Some(orig_fn) = G_ITEM_SET.get() {
                    orig_fn(&pos, item as u32, 0);
                }

                // open boss doors. temp fix! since you can miss the item this way
                let p_flags_global = dll_offset(Offset::FlagsGlobal) as *mut u8;
                *p_flags_global &= 0xFD; // clear boss door flag
            }

            let p_game_mode = (DLL_BASE + 0x964346) as *mut u8;
            p_game_mode.write(1);

            if let Some(orig_fn) = ABADDON_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }

            p_game_mode.write(0);
        } else {
            if let Some(orig_fn) = ABADDON_DEFEAT.get() {
                orig_fn(p_obj_data, a, b, c);
            }
        }
    }
}

// todo: consolidate all *_defeat functions probably...
