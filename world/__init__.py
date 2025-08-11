# import os
import settings
import typing
from .options import cvdosOptions
from .items import item_table
from .locations import location_table
from .regions import create_regions
from .rules import create_rules
from .patch import patch
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, Tutorial

class cvdosItem(Item):  # or from Items import MyGameItem
    game = "cvdos"  # name of the game/world this item is from

class cvdosLocation(Location):  # or from Locations import MyGameLocation
    game = "cvdos"  # name of the game/world this location is in


class MyGameSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("MyGame.sfc")

class cvdosWorld(World):
    """Insert description of the world/game here."""
    game = "cvdos"  # name of the game/world
    options_dataclass = cvdosOptions  # options the player can set
    options: cvdosOptions  # typing hints for option results
    # settings: typing.ClassVar[cvdosSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 0x86420
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for id, name in enumerate(item_table, base_id)}
    location_name_to_id = {name: id for id, name in enumerate(location_table, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "weapons": {"sword", "lance"},
    # }
    item_name_groups = {
        "long_jump": {"Flying Armor soul", "Puppet Master soul", "Malphas soul"},
        "high_jump": {"Malphas soul"},
    }


    def create_regions(self) -> None:
        create_regions(self)

    def create_items(self) -> None:
        for name in item_table:
            self.multiworld.itempool.append(self.create_item(name))

    def create_item(self, item: str) -> Item:
        data = item_table[item]
        return Item(item, data, self.item_name_to_id[item], self.player)

    def set_rules(self) -> None:
        create_rules(self)

    def generate_output(self, output_directory: str) -> None:
        patch(self, output_directory)
