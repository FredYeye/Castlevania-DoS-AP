from BaseClasses import Location
from typing import Union
from dataclasses import dataclass

class cvdosLocation(Location):
    game: str = "cvdos"

@dataclass(frozen=True)
class StaticItem:
    map_id: int
    enm_slot: int

@dataclass(frozen=True)
class Boss:
    id: int

Loc = Union[StaticItem, Boss]

loc_01:  dict[str, Loc] = { "The Lost Village - Pumpkin Pie"        : StaticItem(0x01, 2)  }
loc_03:  dict[str, Loc] = { "The Lost Village - Mace"               : StaticItem(0x03, 5)  }
loc_08b: dict[str, Loc] = { "The Lost Village - High Potion"        : StaticItem(0x08, 4)  }
loc_09b: dict[str, Loc] = { "The Lost Village - Claymore"           : StaticItem(0x09, 2)  }
loc_0C:  dict[str, Loc] = { "The Lost Village - Flying Armor"       : Boss(0x65)           }
loc_0D:  dict[str, Loc] = { "The Lost Village - Potion 2"           : StaticItem(0x0D, 0)  }
loc_0F:  dict[str, Loc] = { "The Lost Village - Potion 1"           : StaticItem(0x0F, 4)  ,
                            "The Lost Village - Short Sword"        : StaticItem(0x0F, 5)  }
loc_12:  dict[str, Loc] = { "The Lost Village - Corn Soup"          : StaticItem(0x12, 3)  }
loc_14:  dict[str, Loc] = { "The Lost Village - Cape"               : StaticItem(0x14, 5)  }
loc_16:  dict[str, Loc] = { "The Lost Village - Crimson Cloak"      : StaticItem(0x16, 11) }
loc_1A:  dict[str, Loc] = { "The Lost Village - Spear"              : StaticItem(0x1A, 3)  }
loc_0E:  dict[str, Loc] = { "The Lost Village - Neck Warmer"        : StaticItem(0x0E, 0)  }
loc_07:  dict[str, Loc] = { "The Lost Village - Caviar"             : StaticItem(0x07, 1)  }

loc_1D:  dict[str, Loc] = { "Demon Guest House - War Fatigues"      : StaticItem(0x1D, 0)  ,
                            "Demon Guest House - UMA News 2-4"      : StaticItem(0x1D, 1)  }
loc_23:  dict[str, Loc] = { "Demon Guest House - Puppet Master"     : Boss(0x6A)           }
loc_24:  dict[str, Loc] = { "Demon Guest House - Magic Seal 3"      : StaticItem(0x24, 0)  }
loc_27:  dict[str, Loc] = { "Demon Guest House - Cestus"            : StaticItem(0x27, 1)  }
loc_2B:  dict[str, Loc] = { "Demon Guest House - Cutall"            : StaticItem(0x2B, 1)  }
loc_2E:  dict[str, Loc] = { "Demon Guest House - Turquoise Stud"    : StaticItem(0x2E, 1)  }
loc_2F:  dict[str, Loc] = { "Demon Guest House - Justaucorps"       : StaticItem(0x2F, 1)  }
loc_32:  dict[str, Loc] = { "Demon Guest House - Great Sword"       : StaticItem(0x32, 1)  }
loc_37:  dict[str, Loc] = { "Demon Guest House - Ring Mail"         : StaticItem(0x37, 2)  }
loc_40:  dict[str, Loc] = { "Demon Guest House - UMA News 2-2"      : StaticItem(0x40, 0)  }
loc_43b: dict[str, Loc] = { "Demon Guest House - High Potion"       : StaticItem(0x43, 0)  }
loc_4C:  dict[str, Loc] = { "Demon Guest House - High Mind Up"      : StaticItem(0x4C, 0)  }
loc_52:  dict[str, Loc] = { "Demon Guest House - UMA News 1-2"      : StaticItem(0x52, 0)  }
loc_39:  dict[str, Loc] = { "Demon Guest House - Paranoia soul"     : Boss(0x6F)           }
loc_22:  dict[str, Loc] = { "Demon Guest House - Olrox's Suit"      : StaticItem(0x22, 0)  }
loc_3D:  dict[str, Loc] = { "Demon Guest House - Mana Prism"        : StaticItem(0x3D, 6)  }
loc_56:  dict[str, Loc] = { "Demon Guest House - Rune Ring"         : StaticItem(0x56, 0)  }
loc_54:  dict[str, Loc] = { "Demon Guest House - Mina's Talisman"   : StaticItem(0x54, 99) } # todo: needs randomization impl!

loc_5D:  dict[str, Loc] = { "Wizardry Lab - Scarf"                  : StaticItem(0x5D, 1)  }
loc_63:  dict[str, Loc] = { "Wizardry Lab - Balore"                 : Boss(0x66)           }
loc_64:  dict[str, Loc] = { "Wizardry Lab - Mind Up"                : StaticItem(0x64, 1)  }
loc_68:  dict[str, Loc] = { "Wizardry Lab - Blunt Sword"            : StaticItem(0x68, 0)  }
loc_6F:  dict[str, Loc] = { "Wizardry Lab - Combat Knife"           : StaticItem(0x6F, 2)  }
loc_71:  dict[str, Loc] = { "Wizardry Lab - Foie Gras"              : StaticItem(0x71, 0)  }
loc_6Db: dict[str, Loc] = { "Wizardry Lab - Aquarius"               : StaticItem(0x6D, 0)  }
loc_7B:  dict[str, Loc] = { "Wizardry Lab - Serenity Robe"          : StaticItem(0x7B, 0)  }
loc_79:  dict[str, Loc] = { "Wizardry Lab - Super Potion"           : StaticItem(0x79, 1)  ,
                            "Wizardry Lab - Bloody Stud"            : StaticItem(0x79, 0)  }
loc_5Db: dict[str, Loc] = { "Wizardry Lab - UMA News 4"             : StaticItem(0x5D, 0)  }
loc_73:  dict[str, Loc] = { "Wizardry Lab - Gold Ring"              : StaticItem(0x73, 0)  }

loc_82:  dict[str, Loc] = { "Garden of Madness - Breastplate"       : StaticItem(0x82, 1)  }
loc_82b: dict[str, Loc] = { "Garden of Madness - Fleuret"           : StaticItem(0x82, 0)  }
loc_83b: dict[str, Loc] = { "Garden of Madness - Elfin Robe"        : StaticItem(0x83, 0)  }
loc_85:  dict[str, Loc] = { "Garden of Madness - Magic Seal 2"      : StaticItem(0x85, 1)  }
loc_9C:  dict[str, Loc] = { "Garden of Madness - Three 7s"          : StaticItem(0x9C, 0)  }
loc_A6:  dict[str, Loc] = { "Garden of Madness - Doppelganger soul" : StaticItem(0xA6, 8)  }
loc_9A:  dict[str, Loc] = { "Garden of Madness - Small Sword"       : StaticItem(0x9A, 0)  }
loc_98b: dict[str, Loc] = { "Garden of Madness - Handgun"           : StaticItem(0x98, 0)  }
loc_86:  dict[str, Loc] = { "Garden of Madness - Ninja Suit"        : StaticItem(0x86, 0)  }

loc_A7:  dict[str, Loc] = { "The Dark Chapel - Halberd"             : StaticItem(0xA7, 0)  } # requires skeleton soul
loc_A8:  dict[str, Loc] = { "The Dark Chapel - Power Belt"          : StaticItem(0xA8, 0)  }
loc_AA:  dict[str, Loc] = { "The Dark Chapel - Long Sword"          : StaticItem(0xAA, 2)  }
loc_AC:  dict[str, Loc] = { "The Dark Chapel - Traveler Cape"       : StaticItem(0xAC, 0)  }
loc_B6:  dict[str, Loc] = { "The Dark Chapel - Malphas"             : Boss(0x67)           }
loc_B8:  dict[str, Loc] = { "The Dark Chapel - Red Scarf"           : StaticItem(0xB8, 2)  }
loc_B9:  dict[str, Loc] = { "The Dark Chapel - Anti-Venom"          : StaticItem(0xB9, 2)  ,
                            "The Dark Chapel - High Mind Up"        : StaticItem(0xB9, 1)  } # todo: bell
loc_BA:  dict[str, Loc] = { "The Dark Chapel - Hoop Earring"        : StaticItem(0xBA, 0)  }
loc_BB:  dict[str, Loc] = { "The Dark Chapel - Potion"              : StaticItem(0xBB, 0)  }
loc_BCb: dict[str, Loc] = { "The Dark Chapel - Kotetsu"             : StaticItem(0xBC, 1)  ,
                            "The Dark Chapel - UMA News 3-2"        : StaticItem(0xBC, 0)  ,
                            "The Dark Chapel - High Potion"         : StaticItem(0xBC, 2)  }

# todo: item will sink...
loc_FE:  dict[str, Loc] = { "Subterranean Hell - Rahab Soul"        : Boss(0x6B)           }
loc_FF:  dict[str, Loc] = { "Subterranean Hell - Chain Mail"        : StaticItem(0xFF, 0)  ,
                            "Subterranean Hell - High Mind Up"      : StaticItem(0xFF, 2)  ,
                            "Subterranean Hell - Rusty Food Tin"    : StaticItem(0xFF, 3)  }
loc_F5:  dict[str, Loc] = { "Subterranean Hell - UMA News 1-3"      : StaticItem(0xF5, 0)  }
loc_F1:  dict[str, Loc] = { "Subterranean Hell - Mushroom"          : StaticItem(0xF1, 0)  }
loc_EA:  dict[str, Loc] = { "Subterranean Hell - Eversing"          : StaticItem(0xEA, 0)  }
loc_ECb: dict[str, Loc] = { "Subterranean Hell - Amanita"           : StaticItem(0xEC, 1)  ,
                            "Subterranean Hell - Mushroom 3"        : StaticItem(0xEC, 0)  }
loc_ECc: dict[str, Loc] = { "Subterranean Hell - Mushroom 2"        : StaticItem(0xEC, 2)  }

loc_CB:  dict[str, Loc] = { "Condemned Tower - Mind Up"             : StaticItem(0xCB, 2)  ,
                            "Condemned Tower - Silver Stud"         : StaticItem(0xCB, 1)  }
loc_C4b: dict[str, Loc] = { "Condemned Tower - Estoc"               : StaticItem(0xC4, 0)  }
loc_C3:  dict[str, Loc] = { "Condemned Tower - UMA News 2-3"        : StaticItem(0xC3, 0)  }
loc_C7h: dict[str, Loc] = { "Condemned Tower - Gergoth"             : Boss(0x6C)           }
loc_C2:  dict[str, Loc] = { "Condemned Tower - Tower Key"           : StaticItem(0xC2, 0)  }
loc_C6:  dict[str, Loc] = { "Condemned Tower - Tasty Meat"          : StaticItem(0xC6, 2)  }

loc_13A: dict[str, Loc] = { "Cursed Clock Tower - Shaman Ring"      : StaticItem(0x13A, 0) }
loc_11B: dict[str, Loc] = { "Cursed Clock Tower - Army Jacket"      : StaticItem(0x11B, 0) }
loc_135: dict[str, Loc] = { "Cursed Clock Tower - Scale Mail"       : StaticItem(0x135, 2) }
loc_134: dict[str, Loc] = { "Cursed Clock Tower - Magic Seal 4"     : StaticItem(0x134, 0) }
loc_137: dict[str, Loc] = { "Cursed Clock Tower - UMA News 3-3"     : StaticItem(0x137, 0) }
loc_12F: dict[str, Loc] = { "Cursed Clock Tower - Zephyr"           : Boss(0x6D)           }

loc_116: dict[str, Loc] = { "Silenced Ruins - Rare Ring"            : StaticItem(0x116, 5) }
loc_10F: dict[str, Loc] = { "Silenced Ruins - Mana Prism"           : StaticItem(0x10F, 3) }
loc_118: dict[str, Loc] = { "Silenced Ruins - Bat Company"          : Boss(0x6E)           }

loc_147: dict[str, Loc] = { "The Pinnacle - Truffle"                : StaticItem(0x147, 2) }
loc_141: dict[str, Loc] = { "The Pinnacle - Durandal"               : StaticItem(0x141, 2) }
loc_14Bb: dict[str, Loc] = { "The Pinnacle - Mana Prism"            : StaticItem(0x14B, 0)  }
loc_14E: dict[str, Loc] = { "The Pinnacle - Lance"                  : StaticItem(0x14E, 3) }
loc_13F: dict[str, Loc] = { "The Pinnacle - Fragarach"              : StaticItem(0x13F, 1) ,
                            "The Pinnacle - Satan's Ring"           : StaticItem(0x13F, 0) }
loc_13E: dict[str, Loc] = { "The Pinnacle - Aguni"                  : Boss(0x70)           }
loc_13D: dict[str, Loc] = { "The Pinnacle - Magic Seal 5"           : StaticItem(0x13D, 0) }

loc_DB:  dict[str, Loc] = { "Mine of Judgment - Death"              : Boss(0x71)           }

loc_164:  dict[str, Loc] = { "The Abyss - Hippogryph soul"          : StaticItem(0x164, 1) }
loc_171:  dict[str, Loc] = { "The Abyss - Abaddon"                  : Boss(0x72)           }

# todo: probably do away with this table in some way
location_table = {
    **loc_01,
    **loc_03,
    **loc_07,
    **loc_08b,
    **loc_09b,
    **loc_0C,
    **loc_0D,
    **loc_0E,
    **loc_0F,
    **loc_12,
    **loc_14,
    **loc_16,
    **loc_1A,
    **loc_1D,
    **loc_22,
    **loc_23,
    **loc_24,
    **loc_27,
    **loc_2B,
    **loc_2E,
    **loc_2F,
    **loc_32,
    **loc_37,
    **loc_39,
    **loc_3D,
    **loc_40,
    **loc_43b,
    **loc_4C,
    **loc_52,
    **loc_54,
    **loc_56,
    **loc_5D,
    **loc_5Db,
    **loc_63,
    **loc_64,
    **loc_68,
    **loc_6Db,
    **loc_6F,
    **loc_71,
    **loc_73,
    **loc_79,
    **loc_7B,
    **loc_82,
    **loc_82b,
    **loc_83b,
    **loc_85,
    **loc_86,
    **loc_98b,
    **loc_9A,
    **loc_9C,
    **loc_A6,
    **loc_A7,
    **loc_A8,
    **loc_AA,
    **loc_AC,
    **loc_B6,
    **loc_B8,
    **loc_B9,
    **loc_BA,
    **loc_BB,
    **loc_BCb,
    **loc_C2,
    **loc_C3,
    **loc_C4b,
    **loc_C6,
    **loc_C7h,
    **loc_CB,
    **loc_DB,
    **loc_EA,
    **loc_ECb,
    **loc_ECc,
    **loc_F1,
    **loc_F5,
    **loc_FE,
    **loc_FF,
    **loc_10F,
    **loc_116,
    **loc_118,
    **loc_11B,
    **loc_12F,
    **loc_134,
    **loc_135,
    **loc_137,
    **loc_13A,
    **loc_13D,
    **loc_13E,
    **loc_13F,
    **loc_141,
    **loc_147,
    **loc_14Bb,
    **loc_14E,
    **loc_164,
    **loc_171,
}
