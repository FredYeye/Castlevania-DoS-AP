from BaseClasses import Location
from typing import NamedTuple, Optional

class cvdosLocation(Location):
    game: str = "cvdos"

location_table = {
    "Lost Village: Flying Armor"       : "Main area",
    "Demon Guest House: Puppet Master" : "Main area",
    "The Dark Chapel: Malphas"         : "Main area",

    "Lost Village: Short Sword"        : "Main area",
    "Lost Village: Potion"             : "Main area",
}
