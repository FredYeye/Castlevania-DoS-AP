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

    # water lever
    map_15 = self.get_region("15")
    water_loc = Location(self.player, "15: Water lever", None, map_15)
    water_loc.place_locked_item(Item("Lowered water level", ItemClassification.progression, None, self.player))
    map_15.locations.append(water_loc)
    set_rule(self.get_entrance("15-16"),
             lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-15"),
             lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-7E"),
             lambda state: state.has("Lowered water level", self.player))

    # balore blocks
    set_rule(self.get_entrance("67-70"),
             lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("70-67"),
             lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("70-6F"),
             lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("67-64"),
             lambda state: state.has("Balore soul", self.player))

    # drawbridge switch
    map_16b = self.get_region("16b")
    drawbridge_switch_loc = Location(self.player, "16b: Drawbridge switch", None, map_16b)
    drawbridge_switch_loc.place_locked_item(Item("Lowered drawbridge", ItemClassification.filler, None, self.player))
    map_16b.locations.append(drawbridge_switch_loc)
    set_rule(self.get_entrance("16-16b"),
             lambda state: state.has("Lowered drawbridge", self.player))
    set_rule(self.get_entrance("16b-16"),
             lambda state: state.has("Lowered drawbridge", self.player))

    visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
