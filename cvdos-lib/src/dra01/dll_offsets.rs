pub enum Offset {
    // functions
    GetEnmList,
    GItemAddRmkItemNum,
    GItemSet,
    GWindowSetMainWindow,
    GWindowSetItemName,
    GergothDefeat,
    ParanoiaDefeat,
    BaloreDefeat,
    EsEnemyDeadSub,
    AbaddonDefeat,
    EsSoulDrop,
    DevEv08_00,
    DraMesgCommGetMessage,

    // "rom" offsets
    ObjAttrTable,

    // "ram" offsets
    DataPtr, // ? points to alldata.bin stuff that's been loaded to memory?
    MagicCirclePos,
    FlagsGlobal,
    InventorySouls,
    InventoryItems,
    InventoryMagicSeals,
    HardMode,
}

impl Offset {
    pub fn get(&self) -> usize {
        use Offset::*;

        match self {
            GetEnmList            => 0x014660,
            GItemAddRmkItemNum    => 0x047B10,
            GItemSet              => 0x047BB0,
            GWindowSetMainWindow  => 0x0716C0,
            GWindowSetItemName    => 0x071990,
            GergothDefeat         => 0x0849B0,
            ParanoiaDefeat        => 0x12D9D0,
            BaloreDefeat          => 0x1365A0,
            EsEnemyDeadSub        => 0x14AAD0,
            EsSoulDrop            => 0x14AE70,
            AbaddonDefeat         => 0x181310,
            DevEv08_00            => 0x1EC730,
            DraMesgCommGetMessage => 0x203F10,

            ObjAttrTable          => 0x2755B0,

            DataPtr               => 0x39BF08,
            MagicCirclePos        => 0x95C7FC,
            FlagsGlobal           => 0x963ED4,
            InventorySouls        => 0x9641C0,
            InventoryItems        => 0x9642AC,
            InventoryMagicSeals   => 0x964344,
            HardMode              => 0x964349,
        }
    }
}
