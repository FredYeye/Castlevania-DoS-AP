pub enum Offset {
    // functions
    GWindowSetMainWindow,
    GetEnmList,
    EsEnemyDeadSub,
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
            GWindowSetMainWindow  => 0x0716C0,
            GetEnmList            => 0x014660,
            EsEnemyDeadSub        => 0x14AAD0,
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
