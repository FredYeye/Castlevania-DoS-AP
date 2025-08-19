from dataclasses import dataclass
from BaseClasses import Item, ItemClassification

class cvdosItem(Item):
    game = "cvdos"

@dataclass
class ItemType():
    item_class: ItemClassification
    is_soul: bool
    item_id: int

item_table: dict[str, ItemType] = {
    "Flying Armor soul"  : ItemType(ItemClassification.progression, True,  0x35),
    "Short Sword"        : ItemType(ItemClassification.filler,      False, 0x52),
    "Potion"             : ItemType(ItemClassification.filler,      False, 0x01),
    "Claymore"           : ItemType(ItemClassification.filler,      False, 0x60),
    "Spear"              : ItemType(ItemClassification.filler,      False, 0x69),
    "Mace"               : ItemType(ItemClassification.filler,      False, 0x72),
    "Cape"               : ItemType(ItemClassification.filler,      False, 0xB0),
    "Potion2"            : ItemType(ItemClassification.filler,      False, 0x01),
    "Corn Soup"          : ItemType(ItemClassification.filler,      False, 0x0D),

    "Mind Up"            : ItemType(ItemClassification.filler,      False, 0x04),
    "Blunt Sword"        : ItemType(ItemClassification.filler,      False, 0x7B),
    "Scarf"              : ItemType(ItemClassification.filler,      False, 0xB9),
    "Balore soul"        : ItemType(ItemClassification.progression, True,  0x74),
    "Combat Knife"       : ItemType(ItemClassification.filler,      False, 0x45),
    "Foie Gras"          : ItemType(ItemClassification.filler,      False, 0x20),

    "Magic Seal 2"       : ItemType(ItemClassification.progression, False, 0x3F),
    "Breastplate"        : ItemType(ItemClassification.filler,      False, 0xA0),
    "Doppelganger"       : ItemType(ItemClassification.useful,      True,  0x76),
    "Fleuret"            : ItemType(ItemClassification.filler,      False, 0x4A),
    "Three 7s"           : ItemType(ItemClassification.filler,      False, 0x99),
}
