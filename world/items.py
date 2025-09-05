from dataclasses import dataclass
from BaseClasses import Item, ItemClassification

class cvdosItem(Item):
    game = "cvdos"

@dataclass(frozen=True)
class ItemType():
    item_class: ItemClassification
    is_soul: bool
    item_id: int

item_table: dict[str, ItemType] = {
    # The Lost Village
    "Flying Armor soul"  : ItemType(ItemClassification.progression, True,  0x35),
    "Short Sword"        : ItemType(ItemClassification.filler,      False, 0x52),
    "Potion"             : ItemType(ItemClassification.filler,      False, 0x01),
    "Claymore"           : ItemType(ItemClassification.filler,      False, 0x60),
    "Spear"              : ItemType(ItemClassification.filler,      False, 0x69),
    "Mace"               : ItemType(ItemClassification.filler,      False, 0x72),
    "Cape"               : ItemType(ItemClassification.filler,      False, 0xB0),
    "Potion2"            : ItemType(ItemClassification.filler,      False, 0x01),
    "Corn Soup"          : ItemType(ItemClassification.filler,      False, 0x0D),
    "Crimson Cloak"      : ItemType(ItemClassification.filler,      False, 0xB2),
    "High Potion"        : ItemType(ItemClassification.filler,      False, 0x02),
    "Pumpkin Pie"        : ItemType(ItemClassification.filler,      False, 0x1C),
    "Neck Warmer"        : ItemType(ItemClassification.filler,      False, 0xBB),
    "Caviar"             : ItemType(ItemClassification.filler,      False, 0x21),

    # Wizardry Lab
    "Mind Up"            : ItemType(ItemClassification.filler,      False, 0x04),
    "Blunt Sword"        : ItemType(ItemClassification.filler,      False, 0x7B),
    "Scarf"              : ItemType(ItemClassification.filler,      False, 0xB9),
    "Balore soul"        : ItemType(ItemClassification.progression, True,  0x74),
    "Combat Knife"       : ItemType(ItemClassification.filler,      False, 0x45),
    "Foie Gras"          : ItemType(ItemClassification.filler,      False, 0x20),
    "Aquarius"           : ItemType(ItemClassification.filler,      False, 0xAD),
    "Serenity Robe"      : ItemType(ItemClassification.filler,      False, 0xAE),
    "Super Potion"       : ItemType(ItemClassification.filler,      False, 0x03),
    "Bloody Stud"        : ItemType(ItemClassification.filler,      False, 0xC3),
    "UMA News 4"         : ItemType(ItemClassification.filler,      False, 0x39),
    "Gold Ring"          : ItemType(ItemClassification.filler,      False, 0xCD),

    # Garden of Madness
    "Magic Seal 2"       : ItemType(ItemClassification.progression, False, 0x3F),
    "Breastplate"        : ItemType(ItemClassification.filler,      False, 0xA0),
    "Doppelganger soul"  : ItemType(ItemClassification.useful,      True,  0x76),
    "Fleuret"            : ItemType(ItemClassification.filler,      False, 0x4A),
    "Three 7s"           : ItemType(ItemClassification.filler,      False, 0x99),
    "Elfin Robe"         : ItemType(ItemClassification.filler,      False, 0xAB),
    "Small Sword"        : ItemType(ItemClassification.filler,      False, 0x4C),
    "Handgun"            : ItemType(ItemClassification.filler,      False, 0x88),
    "Ninja Suit"         : ItemType(ItemClassification.filler,      False, 0x98),

    # The Dark Chapel
    "Potion3"            : ItemType(ItemClassification.filler,      False, 0x01),
    "Anti-Venom"         : ItemType(ItemClassification.filler,      False, 0x07),
    "Malphas soul"       : ItemType(ItemClassification.progression, True,  0x75),
    "Hoop Earring"       : ItemType(ItemClassification.filler,      False, 0xBF),
    "High Mind up"       : ItemType(ItemClassification.filler,      False, 0x05),
    "Power Belt"         : ItemType(ItemClassification.filler,      False, 0xBC),
    "Long Sword"         : ItemType(ItemClassification.filler,      False, 0x54),
    "Traveler Cape"      : ItemType(ItemClassification.filler,      False, 0xB1),
    "Red Scarf"          : ItemType(ItemClassification.filler,      False, 0xBA),
    "Halberd"            : ItemType(ItemClassification.filler,      False, 0x6B),
    "Kotetsu"            : ItemType(ItemClassification.filler,      False, 0x7D),
    "UMA News 3-2"       : ItemType(ItemClassification.filler,      False, 0x37),
    "High Potion3"       : ItemType(ItemClassification.filler,      False, 0x02),

    # Demon Guest House
    "High Mind up2"      : ItemType(ItemClassification.filler,      False, 0x05),
    "Cestus"             : ItemType(ItemClassification.filler,      False, 0x84),
    "Cutall"             : ItemType(ItemClassification.filler,      False, 0x47),
    "Turquoise Stud"     : ItemType(ItemClassification.filler,      False, 0xC0),
    "Justaucorps"        : ItemType(ItemClassification.filler,      False, 0x9A),
    "Great Sword"        : ItemType(ItemClassification.filler,      False, 0x62),
    "Ring Mail"          : ItemType(ItemClassification.filler,      False, 0xA1),
    "UMA News 1-2"       : ItemType(ItemClassification.filler,      False, 0x30),
    "War Fatigues"       : ItemType(ItemClassification.filler,      False, 0x97),
    "UMA News 2-4"       : ItemType(ItemClassification.filler,      False, 0x35),
    "High Potion2"       : ItemType(ItemClassification.filler,      False, 0x02),
    "UMA News 2-2"       : ItemType(ItemClassification.filler,      False, 0x33),
    "Magic Seal 3"       : ItemType(ItemClassification.progression, False, 0x40),
    "Puppet Master soul" : ItemType(ItemClassification.progression, True,  0x00),
    "Paranoia soul"      : ItemType(ItemClassification.progression, True,  0x02),
    "Olrox's Suit"       : ItemType(ItemClassification.filler,      False, 0x9D),
    "Mana Prism2"        : ItemType(ItemClassification.filler,      False, 0x06),
    "Rune Ring"          : ItemType(ItemClassification.filler,      False, 0xCB),
    "Mina's Talisman"    : ItemType(ItemClassification.progression, False, 0xC7),

    # Subterranean Hell
    "Rahab soul"         : ItemType(ItemClassification.progression, True,  0x77),
    "Chain Mail"         : ItemType(ItemClassification.filler,      False, 0xA3),
    "High Mind Up3"      : ItemType(ItemClassification.filler,      False, 0x05),
    "Rusty Food Tin"     : ItemType(ItemClassification.filler,      False, 0x2B),
    "UMA News 1-3"       : ItemType(ItemClassification.filler,      False, 0x31),
    "Mushroom"           : ItemType(ItemClassification.filler,      False, 0x0C),
    "Eversing"           : ItemType(ItemClassification.filler,      False, 0xA7),
    "Mushroom2"          : ItemType(ItemClassification.filler,      False, 0x0C),
    "Amanita"            : ItemType(ItemClassification.filler,      False, 0x28),
    "Mushroom3"          : ItemType(ItemClassification.filler,      False, 0x0C),
                                    
    # Condemned Tower
    "Mind Up2"           : ItemType(ItemClassification.filler,      False, 0x04),
    "Silver Stud"        : ItemType(ItemClassification.filler,      False, 0xC1),
    "Estoc"              : ItemType(ItemClassification.filler,      False, 0x4D),
    "UMA News 2-3"       : ItemType(ItemClassification.filler,      False, 0x34),
    "Gergoth soul"       : ItemType(ItemClassification.filler,      True,  0x57),
    "Tower Key"          : ItemType(ItemClassification.progression, False, 0x3A),
    "Tasty Meat"         : ItemType(ItemClassification.filler,      False, 0x0A),
                                    
    # Cursed Clock Tower
    "Shaman Ring"        : ItemType(ItemClassification.filler,      False, 0xCC),
    "Army Jacket"        : ItemType(ItemClassification.filler,      False, 0x9B),
    "Scale Mail"         : ItemType(ItemClassification.filler,      False, 0xA2),
    "Magic Seal 4"       : ItemType(ItemClassification.progression, False, 0x41),
    "UMA News 3-3"       : ItemType(ItemClassification.filler,      False, 0x38),
    "Zephyr soul"        : ItemType(ItemClassification.progression, True,  0x01),

    # Silenced Ruins
    "Rare Ring"          : ItemType(ItemClassification.filler,      False, 0xC9),
    "Mana Prism"         : ItemType(ItemClassification.filler,      False, 0x06),
    "Bat Company soul"   : ItemType(ItemClassification.progression, True,  0x36),

    # The Pinnacle
    "Truffle"            : ItemType(ItemClassification.filler,      False, 0x22),
    "Durandal"           : ItemType(ItemClassification.filler,      False, 0x63),
    "Mana Prism3"        : ItemType(ItemClassification.filler,      False, 0x06),
    "Lance"              : ItemType(ItemClassification.filler,      False, 0x6C),
    "Fragarach"          : ItemType(ItemClassification.filler,      False, 0x55),
    "Satan's Ring"       : ItemType(ItemClassification.filler,      False, 0xC8),
    "Aguni soul"         : ItemType(ItemClassification.filler,      True , 0x2B),
    "Magic Seal 5"       : ItemType(ItemClassification.progression, False, 0x42), # 42 is gorgon soul. but why?

    # Mine of Judgment
    "Death soul"         : ItemType(ItemClassification.filler,      True,  0x59),

    # The Abyss
    "Hippogryph soul"    : ItemType(ItemClassification.progression, True,  0x78),
    "Abaddon soul"       : ItemType(ItemClassification.filler,      True,  0x2C),
}
