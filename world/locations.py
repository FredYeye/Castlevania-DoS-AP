from BaseClasses import Location
from typing import NamedTuple, Optional, Union
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

loc_lv01: dict[str, Loc] = {
    "Lost Village - Potion 1"     : StaticItem(0x0F, 4),
    "Lost Village - Short Sword"  : StaticItem(0x0F, 5),
    "Lost Village - Flying Armor" : Boss(0x65),
}

loc_lv02: dict[str, Loc] = {
    "Lost Village - Claymore"     : StaticItem(0x09, 2),
    "Lost Village - Spear"        : StaticItem(0x1A, 3),
    "Lost Village - Mace"         : StaticItem(0x03, 5),
    "Lost Village - Cape"         : StaticItem(0x14, 5),
    "Lost Village - Potion 2"     : StaticItem(0x0D, 0),

    "Wizardry Lab - Mind Up"      : StaticItem(0x64, 1),
}

loc_others: dict[str, Loc] = {
    "The Dark Chapel - Malphas"         : Boss(0x67),
    "Demon Guest House - Puppet Master" : Boss(0x6A),
}

location_table = {
    **loc_lv01,
    **loc_lv02,
    **loc_others,
}
