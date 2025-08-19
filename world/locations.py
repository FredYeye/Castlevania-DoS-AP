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

loc_03: dict[str, Loc] = {
    "Lost Village - Mace"         : StaticItem(0x03, 5),
}

loc_09: dict[str, Loc] = {
    "Lost Village - Claymore"     : StaticItem(0x09, 2),
}

loc_0C: dict[str, Loc] = {
    "Lost Village - Flying Armor" : Boss(0x65),
}

loc_0D: dict[str, Loc] = {
    "Lost Village - Potion 2"     : StaticItem(0x0D, 0),
}

loc_0F: dict[str, Loc] = {
    "Lost Village - Potion 1"     : StaticItem(0x0F, 4),
    "Lost Village - Short Sword"  : StaticItem(0x0F, 5),
}

loc_12: dict[str, Loc] = {
    "Lost Village - Corn Soup"    : StaticItem(0x12, 3),
}

loc_14: dict[str, Loc] = {
    "Lost Village - Cape"         : StaticItem(0x14, 5),
}

loc_1A: dict[str, Loc] = {
    "Lost Village - Spear"        : StaticItem(0x1A, 3),
}

loc_5D: dict[str, Loc] = {
    "Wizardry Lab - Scarf"        : StaticItem(0x5D, 1),
}

loc_63: dict[str, Loc] = {
    "Wizardry Lab - Balore"       : Boss(0x66),
}

loc_64: dict[str, Loc] = {
    "Wizardry Lab - Mind Up"      : StaticItem(0x64, 1),
}

loc_68: dict[str, Loc] = {
    "Wizardry Lab - Blunt Sword"  : StaticItem(0x68, 0),
}

loc_6F: dict[str, Loc] = {
    "Wizardry Lab - Combat Knife" : StaticItem(0x6F, 2),
}

loc_71: dict[str, Loc] = {
    "Wizardry Lab - Foie Gras" : StaticItem(0x71, 0),
}

loc_82: dict[str, Loc] = {
    "Garden of Madness - Breastplate" : StaticItem(0x82, 1),
}

loc_82b: dict[str, Loc] = {
    "Garden of Madness - Fleuret" : StaticItem(0x82, 0),
}

loc_85: dict[str, Loc] = {
    "Garden of Madness - Magic Seal 2" : StaticItem(0x85, 1),
}

loc_9C: dict[str, Loc] = {
    "Garden of Madness - Three 7s" : StaticItem(0x9C, 0),
}

loc_A6: dict[str, Loc] = {
    "Garden of Madness - Doppelganger" : StaticItem(0xA6, 8),
}

location_table = {
    **loc_03,
    **loc_09,
    **loc_0C,
    **loc_0D,
    **loc_0F,
    **loc_12,
    **loc_14,
    **loc_1A,
    **loc_5D,
    **loc_63,
    **loc_64,
    **loc_68,
    **loc_6F,
    **loc_71,
    **loc_82,
    **loc_82b,
    **loc_85,
    **loc_9C,
    **loc_A6,
}
