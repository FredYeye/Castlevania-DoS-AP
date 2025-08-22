from worlds.generic.Rules import set_rule
from BaseClasses import ItemClassification, Item, Location
from Utils import visualize_regions

# todo: clean up this mess

def create_rules(self) -> None:
    set_rule(self.get_entrance("09-09b"), lambda state: state.has_group("long_jump", self.player))
    set_rule(self.get_entrance("0D-10"), lambda state: state.has_group("long_jump", self.player))
    set_rule(self.get_entrance("26-1F"), lambda state: state.has_group("long_jump", self.player))
    set_rule(self.get_entrance("42-3B"), lambda state: state.has_group("long_jump", self.player))

    set_rule(self.get_entrance("05-05b"), lambda state: state.has("Malphas soul", self.player) and
                                                        state.has("Puppet Master soul", self.player))

    # water lever
    map_15 = self.get_region("15")
    water_loc = Location(self.player, "15: Water lever", None, map_15)
    water_loc.place_locked_item(Item("Lowered water level", ItemClassification.progression, None, self.player))
    map_15.locations.append(water_loc)
    set_rule(self.get_entrance("15-16"), lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-15"), lambda state: state.has("Lowered water level", self.player))
    set_rule(self.get_entrance("16-7E"), lambda state: state.has("Lowered water level", self.player))

    # balore blocks
    set_rule(self.get_entrance("67-70"), lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("70-67"), lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("70-6F"), lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("67-64"), lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("6C-71"), lambda state: state.has("Balore soul", self.player))
    set_rule(self.get_entrance("6C-72"), lambda state: state.has("Balore soul", self.player) or
                                                       state.has("Malphas soul", self.player))

    # drawbridge switch
    map_16b = self.get_region("16b")
    drawbridge_switch_loc = Location(self.player, "16b: Drawbridge switch", None, map_16b)
    drawbridge_switch_loc.place_locked_item(Item("Lowered drawbridge", ItemClassification.filler, None, self.player))
    map_16b.locations.append(drawbridge_switch_loc)
    set_rule(self.get_entrance("16-16b"), lambda state: state.has("Lowered drawbridge", self.player) or
                                                        state.has("Malphas soul", self.player))
    set_rule(self.get_entrance("16b-16"), lambda state: state.has("Lowered drawbridge", self.player))

    set_rule(self.get_entrance("B1-B7"), lambda state: state.has("Magic Seal 2", self.player))
    set_rule(self.get_entrance("BA-B6"), lambda state: state.has("Magic Seal 2", self.player))
    set_rule(self.get_entrance("8E-8D"), lambda state: state.has("Magic Seal 2", self.player))
    set_rule(self.get_entrance("3E-23"), lambda state: state.has("Magic Seal 3", self.player))
    set_rule(self.get_entrance("FC-FE"), lambda state: state.has("Magic Seal 3", self.player))
    set_rule(self.get_entrance("C8b-C7h"), lambda state: state.has("Magic Seal 3", self.player))

    set_rule(self.get_location("The Dark Chapel - Hoop Earring"), lambda state: state.has("Malphas soul", self.player))

    set_rule(self.get_location("The Dark Chapel - High Mind Up"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_location("The Dark Chapel - Power Belt"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_location("The Dark Chapel - Long Sword"), lambda state: state.has("Malphas soul", self.player) or
                                                                              state.has("Flying Armor soul", self.player) and
                                                                              state.has("Puppet Master soul", self.player))

    set_rule(self.get_location("The Lost Village - Crimson Cloak"), lambda state: state.has("Malphas soul", self.player) or
                                                                           state.has("Flying Armor soul", self.player) and
                                                                           state.has("Puppet Master soul", self.player))

    set_rule(self.get_entrance("08-08b"), lambda state: state.has("Malphas soul", self.player) or
                                                        state.has("Flying Armor soul", self.player) and
                                                        state.has("Puppet Master soul", self.player))

    set_rule(self.get_entrance("83-83b"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("8F-8E"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("4D-4C"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("4Cb-4B"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("38-21"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("38-37"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("38-2E"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("38-2F"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("38-32"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("38-20"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("20-26"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("1E-1D"), lambda state: state.has("Malphas soul", self.player))

    set_rule(self.get_location("Demon Guest House - War Fatigues"), lambda state: state.has("Balore soul", self.player) and
                                                                           state.has_group("height", self.player))
    set_rule(self.get_location("Demon Guest House - UMA News 2-4"), lambda state: state.has("Balore soul", self.player) and
                                                                           state.has_group("height", self.player))
    
    set_rule(self.get_entrance("43b-42"), lambda state: state.has("Malphas soul", self.player))

    set_rule(self.get_entrance("41-3A"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("3A-3E"), lambda state: state.has("Malphas soul", self.player))

    set_rule(self.get_entrance("4C-4Cb"), lambda state: state.has("Puppet Master soul", self.player))
    set_rule(self.get_entrance("4Cb-4C"), lambda state: state.has("Puppet Master soul", self.player))
    
    set_rule(self.get_entrance("45-45b"), lambda state: state.has("Puppet Master soul", self.player))
    set_rule(self.get_entrance("45b-45"), lambda state: state.has("Puppet Master soul", self.player))

    set_rule(self.get_entrance("AF-AFb"), lambda state: state.has("Puppet Master soul", self.player))
    set_rule(self.get_entrance("AFb-AF"), lambda state: state.has("Puppet Master soul", self.player))

    # Rahab soul
    # todo: try PM...
    set_rule(self.get_entrance("100-FE"), lambda state: state.has("Rahab soul", self.player))

    set_rule(self.get_entrance("100-FF"), lambda state: state.has("Rahab soul", self.player))
    set_rule(self.get_entrance("FF-100"), lambda state: state.has("Rahab soul", self.player))

    set_rule(self.get_entrance("FF-FD"), lambda state: state.has("Rahab soul", self.player))
    set_rule(self.get_entrance("FD-FF"), lambda state: state.has("Rahab soul", self.player) and
                                                       state.has_group("height", self.player))
    
    set_rule(self.get_entrance("FD-FA"), lambda state: state.has("Rahab soul", self.player))

    set_rule(self.get_entrance("F8-F8b"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("F9-F8"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("F7-F8b"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("F7-F3"), lambda state: state.has_group("height", self.player) or 
                                                       state.has("Rahab Soul", self.player))
    
    set_rule(self.get_location("Subterranean Hell - UMA News 1-3"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("F5-F6"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_location("Garden of Madness - Small Sword"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("99-99b"), lambda state: state.has("Rahab soul", self.player))
    set_rule(self.get_entrance("99b-99"), lambda state: state.has("Rahab soul", self.player))

    set_rule(self.get_entrance("91-91b"), lambda state: state.has("Rahab soul", self.player))
    set_rule(self.get_entrance("91b-91"), lambda state: state.has("Rahab soul", self.player))

    set_rule(self.get_entrance("F1-F2"), lambda state: state.has_group("long_jump", self.player))
    set_rule(self.get_entrance("ED-EF"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("EC-EA"), lambda state: state.has("Malphas soul", self.player) or
                                                       state.has("Flying Armor soul", self.player) and
                                                       state.has("Puppet Master soul", self.player))
    
    set_rule(self.get_entrance("EC-ECb"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("ECc-ECb"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("ECd-ECc"), lambda state: state.has_group("height", self.player))
    
    set_rule(self.get_entrance("EE-103"), lambda state: state.has_group("long_jump", self.player))

    set_rule(self.get_entrance("B9-B9b"), lambda state: state.has("Puppet Master soul", self.player))
    set_rule(self.get_entrance("B9b-B9"), lambda state: state.has("Puppet Master soul", self.player))
    set_rule(self.get_entrance("BCb-B9b"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_location("The Dark Chapel - Kotetsu"), lambda state: state.has("Malphas soul", self.player) and
                                                                           state.has("Puppet Master soul", self.player))
    set_rule(self.get_location("The Dark Chapel - UMA News 3-2"), lambda state: state.has_group("long_jump", self.player)) # technically can be reached with a backdash jump, but probably not fun

    # BCb switch
    map_BCb = self.get_region("BCb")
    switch_loc = Location(self.player, "BCb: Gate Switch", None, map_BCb)
    switch_loc.place_locked_item(Item("Opened gate", ItemClassification.filler, None, self.player)) # filler?
    map_BCb.locations.append(switch_loc)
    set_rule(self.get_entrance("BC-BCb"), lambda state: state.has("Opened gate", self.player))
    set_rule(self.get_entrance("BCb-BC"), lambda state: state.has("Opened gate", self.player))

    set_rule(self.get_location("Condemned Tower - Silver Stud"), lambda state: state.has_group("height", self.player))

    set_rule(self.get_entrance("CB-C7b"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C5-C7c"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("CA-C7d"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C4-C4b"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C9-C7f"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_location("Condemned Tower - UMA News 2-3"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C3-C0"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C3-C7g"), lambda state: state.has_group("height", self.player))
    set_rule(self.get_entrance("C8-C8b"), lambda state: state.has_group("height", self.player))

    visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
