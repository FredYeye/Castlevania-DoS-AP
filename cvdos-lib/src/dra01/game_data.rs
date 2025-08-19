pub const OBJ_ATTR_LENGTH: usize = 118;

#[repr(C)]
pub struct ObjAttr {
    create_fn: u64,
    update_fn: u64,
    pub item1: u16,
    item2: u16,
    unk1: u8,
    unk2: u8,
    hp: u16,
    mp: u16,
    xp: u16,
    soul_rarity: u8,
    attack: u8,
    defense: u8,
    pub item_rarity: u8,
    unk3: u8,
    unk4: u8,
    pub soul_id: u8,
    unk5: u8,
    weakness: u32,
    resistance: u32,
    padding: u32,
}

#[repr(C)]
pub struct EnmSetData {
    x: i16,
    y: i16,
    id: u8,
    pub type1: u8,
    pub type2: u8,
    unk: u8,
    pub var1: u16,
    pub var2: u16,
}

#[repr(C)]
pub struct MagicCirclePos {
    pub x: u32,
    pub y: u32,
}

pub enum Enemy {
    Zombie,
    Warg,
    FlyingArmor,
    Balore,
    Malphas,
    PuppetMaster,
}

impl Enemy {
    pub fn id(&self) -> u8 {
        use Enemy::*;
        match self {
            Zombie => 0x00,
            Warg => 0x08,
            FlyingArmor => 0x65,
            Balore => 0x66,
            Malphas => 0x67,
            PuppetMaster => 0x6A,
        }
    }
}
