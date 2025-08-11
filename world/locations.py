from BaseClasses import Location
from typing import NamedTuple, Optional

class cvdosLocation(Location):
    game: str = "cvdos"

loc_lv01 = {
    "Lost Village - Flying Armor"       : "LV01",
    "Lost Village - Potion"             : "LV01",
    "Lost Village - Short Sword"        : "LV01",
}

loc_others = {
    "Demon Guest House - Puppet Master" : "Main area",
    "The Dark Chapel - Malphas"         : "Main area",
}

location_table = {
    **loc_lv01,
    **loc_others,
}
