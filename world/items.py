from BaseClasses import Item, ItemClassification
from typing import NamedTuple

class cvdosItem(NamedTuple):
    item_class: ItemClassification
    is_soul: bool
    item_id: int

item_table: dict[str, cvdosItem] = {
    "Flying Armor soul"  : cvdosItem(ItemClassification.progression, True, 0x35),
    "Short Sword"        : cvdosItem(ItemClassification.filler, False, 0x52),
    "Potion"             : cvdosItem(ItemClassification.filler, False, 0x01),

    "Claymore"           : cvdosItem(ItemClassification.filler, False, 0x60),
    "Spear"              : cvdosItem(ItemClassification.filler, False, 0x69),
    "Mace"               : cvdosItem(ItemClassification.filler, False, 0x72),
    "Cape"               : cvdosItem(ItemClassification.filler, False, 0xB0),
    "Potion2"            : cvdosItem(ItemClassification.filler, False, 0x01),
    "Mind Up"            : cvdosItem(ItemClassification.filler, False, 0x04),

    "Malphas soul"       : cvdosItem(ItemClassification.progression, True, 0x75),
    "Puppet Master soul" : cvdosItem(ItemClassification.progression, True, 0x00),
}
