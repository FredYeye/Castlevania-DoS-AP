from worlds.generic.Rules import set_rule
from BaseClasses import ItemClassification, Item, Location
from Utils import visualize_regions

def create_rules(self) -> None:
    set_rule(self.get_location("Lost Village - Claymore"),
             lambda state: state.has_group("long_jump", self.player))

    set_rule(self.get_entrance("09-1A"),
             lambda state: state.has_group("long_jump", self.player))
    set_rule(self.get_entrance("0D-10"),
             lambda state: state.has_group("long_jump", self.player))

    map_15 = self.get_region("15")
    water_loc = Location(self.player, "15: Water switch", None, map_15)
    water_loc.place_locked_item(Item("Lowered water level", ItemClassification.progression, None, self.player))
    map_15.locations.append(water_loc)
    set_rule(self.get_entrance("15-16"),
             lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-15"),
             lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-7E"),
             lambda state: state.has("Lowered water level", self.player))

    visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
