pub enum Offset {
    // functions
    GWindowSetMainWindow,
    EsEnemyDeadSub,
    DraMesgCommGetMessage,

    // "rom" offsets
    ObjAttrTable,

    // "ram" offsets
    FlagsGlobal,
    InventorySouls,
    InventoryItems,
    InventoryMagicSeals,
}

impl Offset {
    pub fn get(&self) -> usize {
        use Offset::*;

        match self {
            GWindowSetMainWindow  => 0x0716C0,
            EsEnemyDeadSub        => 0x14AAD0,
            DraMesgCommGetMessage => 0x203F10,

            ObjAttrTable          => 0x2755B0,

            FlagsGlobal           => 0x963ED4,
            InventorySouls        => 0x9641C0,
            InventoryItems        => 0x9642AC,
            InventoryMagicSeals   => 0x964344,
        }
    }
}