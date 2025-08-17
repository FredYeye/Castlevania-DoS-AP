import settings
from .options import cvdosOptions
from .items import item_table
from .locations import location_table
from .regions import create_regions
from .rules import create_rules
from .patch import patch
from worlds.AutoWorld import World
from BaseClasses import Item

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

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for id, name in enumerate(item_table, 1)}
    location_name_to_id = {name: id for id, name in enumerate(location_table, 1)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "long_jump": {"Flying Armor soul"},
    }

    def create_regions(self) -> None:
        create_regions(self)

    def create_items(self) -> None:
        for name in item_table:
            self.multiworld.itempool.append(self.create_item(name))

    def create_item(self, item: str) -> Item:
        data = item_table[item].item_class
        return Item(item, data, self.item_name_to_id[item], self.player)

    def set_rules(self) -> None:
        create_rules(self)
        # print("create rules")
        # set_rule(self.get_entrance("09-1A"),
        #         lambda state: state.has_group("long_jump", self.player))
        # set_rule(self.get_entrance("0D-10"),
        #         lambda state: state.has_group("long_jump", self.player))

        # map_15 = self.get_region("15")
        # water_loc = Location(self.player, "Water switch", None, map_15)
        # water_loc.place_locked_item(Item("Lowered water level", ItemClassification.progression, None, self.player))
        # map_15.locations.append(water_loc)

    def generate_output(self, output_directory: str) -> None:
        patch(self, output_directory)
