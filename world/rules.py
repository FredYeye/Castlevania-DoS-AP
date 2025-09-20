from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState, ItemClassification, Item, Location
from Utils import visualize_regions
from .regions import EntrReq, maps

def medium_height(state: CollectionState, p: int) -> bool:
    return state.has("Malphas soul", p) or state.has("flight", p)

def big_height(state: CollectionState, p: int) -> bool:
    return state.has("Malphas soul", p) and state.has("Puppet Master soul", p) or state.has("flight", p)

def height_and_distance(state: CollectionState, p: int) -> bool: # todo: name?
    return medium_height(state, p) or state.has("Flying Armor soul", p) and state.has("Puppet Master soul", p)

def create_rules(self) -> None:
    p = self.player

    for map_id, map_data in maps.items():
        for conn in map_data.connections:
            if conn.req != None:
                entrance_str = map_id + "-" + conn.destination + conn.extra_id
                entrance = self.get_entrance(entrance_str)

                match conn.req:
                    case EntrReq.HEIGHT:
                        set_rule(entrance, lambda state: state.has_group("height", p))

                    case EntrReq.MEDIUM_HEIGHT:
                        set_rule(entrance, lambda state: medium_height(state, p))

                    case EntrReq.BIG_HEIGHT:
                        set_rule(entrance, lambda state: big_height(state, p))

                    case EntrReq.HEIGHT_AND_DISTANCE:
                        set_rule(entrance, lambda state: height_and_distance(state, p))

                    case EntrReq.DISTANCE:
                        set_rule(entrance, lambda state: state.has_group("long_jump", p))

                    case EntrReq.BALORE:
                        set_rule(entrance, lambda state: state.has("Balore soul", p))

                    case EntrReq.MAGIC_SEAL_2:
                        set_rule(entrance, lambda state: state.has("Magic Seal 2", p))

                    case EntrReq.MAGIC_SEAL_3:
                        set_rule(entrance, lambda state: state.has("Magic Seal 3", p))

                    case EntrReq.MAGIC_SEAL_4:
                        set_rule(entrance, lambda state: state.has("Magic Seal 4", p))
                    
                    case EntrReq.MAGIC_SEAL_5:
                        set_rule(entrance, lambda state: state.has("Magic Seal 5", p))

                    case EntrReq.SMALL:
                        set_rule(entrance, lambda state: state.has_group("small", p))

                    case EntrReq.RAHAB:
                        set_rule(entrance, lambda state: state.has("Rahab soul", p))

                    case EntrReq.ZEPHYR:
                        set_rule(entrance, lambda state: state.has("Zephyr soul", p))

                    case EntrReq.BIGGER_HEIGHT:
                        set_rule(entrance, lambda state: state.has_group("flight", p))

                    case EntrReq.BALORE_OR_MEDIUM_HEIGHT:
                        set_rule(entrance, lambda state: state.has("Balore soul", p) or
                                                         medium_height(state, p))

                    case EntrReq.RAHAB_OR_HEIGHT:
                        set_rule(entrance, lambda state: state.has("Rahab Soul", p) or
                                                         state.has_group("height", p))

                    case EntrReq.RAHAB_AND_HEIGHT:
                        set_rule(entrance, lambda state: state.has("Rahab Soul", p) and
                                                         state.has_group("height", p))
                    
                    case EntrReq.MAGIC_SEAL_5_AND_HEIGHT:
                        set_rule(entrance, lambda state: state.has("Magic Seal 5", p) and
                                                  state.has_group("height", p))
                    
                    case EntrReq.MAGIC_SEAL_3_AND_RAHAB:
                        set_rule(entrance, lambda state: state.has("Magic Seal 3", p) and
                                                  state.has("Rahab soul", p))

    set_rule(self.get_location("The Dark Chapel - Hoop Earring"), lambda state: medium_height(state, p))
    set_rule(self.get_location("The Dark Chapel - High Mind Up"), lambda state: state.has_group("height", p))
    set_rule(self.get_location("The Dark Chapel - Power Belt"), lambda state: state.has_group("height", p))
    set_rule(self.get_location("The Dark Chapel - Long Sword"), lambda state: height_and_distance(state, p))
    set_rule(self.get_location("The Dark Chapel - Kotetsu"), lambda state: big_height(state, p))
    set_rule(self.get_location("The Dark Chapel - UMA News 3-2"), lambda state: state.has_group("long_jump", p)) # technically can be reached with a backdash jump, but probably not fun

    set_rule(self.get_location("The Lost Village - Crimson Cloak"), lambda state: height_and_distance(state, p))

    set_rule(self.get_location("Demon Guest House - War Fatigues"), lambda state: state.has("Balore soul", p) and
                                                                           state.has_group("height", p))
    set_rule(self.get_location("Demon Guest House - UMA News 2-4"), lambda state: state.has("Balore soul", p) and
                                                                           state.has_group("height", p))

    set_rule(self.get_location("Subterranean Hell - UMA News 1-3"), lambda state: state.has_group("height", p))
    set_rule(self.get_location("Garden of Madness - Small Sword"), lambda state: state.has_group("height", p))

    set_rule(self.get_location("Condemned Tower - Silver Stud"), lambda state: state.has_group("height", p))
    set_rule(self.get_location("Condemned Tower - UMA News 2-3"), lambda state: state.has_group("height", p))

    set_rule(self.get_location("Silenced Ruins - Rare Ring"), lambda state: state.has("Balore soul", p))

    set_rule(self.get_location("Wizardry Lab - Serenity Robe"), lambda state: state.has("Rahab soul", p))
    set_rule(self.get_location("Wizardry Lab - Super Potion"), lambda state: state.has("Rahab soul", p))
    set_rule(self.get_location("Wizardry Lab - Bloody Stud"), lambda state: state.has("Rahab soul", p))
    set_rule(self.get_location("Demon Guest House - Mana Prism"), lambda state: state.has("Paranoia soul", p)), # mini paranoia must also be defeated
    set_rule(self.get_location("The Pinnacle - Aguni"), lambda state: state.has("Paranoia soul", p)),

    # height is technically not needed as you can get the item and suspend out
    set_rule(self.get_location("The Abyss - Hippogryph soul"), lambda state: state.has_group("height", p)),

    # water lever
    region = self.get_region("15")
    loc = Location(p, "15: Water lever", None, region)
    loc.place_locked_item(Item("Lowered water level", ItemClassification.progression, None, p))
    region.locations.append(loc)
    set_rule(self.get_entrance("15-16"), lambda state: state.has("Lowered water level", p))
    set_rule(self.get_entrance("16-15"), lambda state: state.has("Lowered water level", p))
    set_rule(self.get_entrance("16-7E"), lambda state: state.has("Lowered water level", p))

    # drawbridge switch
    region = self.get_region("16b")
    loc = Location(p, "16b: Drawbridge switch", None, region)
    loc.place_locked_item(Item("Lowered drawbridge", ItemClassification.filler, None, p))
    region.locations.append(loc)
    set_rule(self.get_entrance("16-16b"), lambda state: state.has("Lowered drawbridge", p) or
                                                        medium_height(state, p))
    set_rule(self.get_entrance("16b-16"), lambda state: state.has("Lowered drawbridge", p))

    # BCb switch
    region = self.get_region("BCb")
    loc = Location(p, "BCb: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (TDC)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("BC-BCb"), lambda state: state.has("Opened gate (TDC)", p))
    set_rule(self.get_entrance("BCb-BC"), lambda state: state.has("Opened gate (TDC)", p))

    # todo: upon defeating gergoth, the player drops to C7 and new access rules
    # should be set for traversing the C7_ regions
    set_rule(self.get_entrance("C7h-C2"), lambda state: state.has_group("long_jump", p) or
                                                        state.has_group("long_jump_no_flight", p, 2))

    set_rule(self.get_entrance("C0-C0b"), lambda state: state.has("Tower Key", p))
    set_rule(self.get_entrance("C0b-C0"), lambda state: state.has("Tower Key", p))

    # 8Cb switch
    region = self.get_region("8Cb")
    loc = Location(p, "8Cb: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (GoM)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("8C-8Cb"), lambda state: state.has("Opened gate (GoM)", p))
    set_rule(self.get_entrance("8Cb-8C"), lambda state: state.has("Opened gate (GoM)", p))

    # 129b switch
    map_129b = self.get_region("129b")
    switch_loc = Location(p, "129b: Gate Switch", None, map_129b)
    switch_loc.place_locked_item(Item("Opened gate (CCT)", ItemClassification.filler, None, p)) # todo: filler?
    map_129b.locations.append(switch_loc)
    set_rule(self.get_entrance("129-129b"), lambda state: state.has("Opened gate (CCT)", p))
    set_rule(self.get_entrance("129b-129"), lambda state: state.has("Opened gate (CCT)", p))
    set_rule(self.get_entrance("129b-128"), lambda state: state.has("Opened gate (CCT)", p) and
                                                          state.has_group("height", p))

    # F9b switch
    region = self.get_region("F9b")
    loc = Location(p, "F9b: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (SH)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    # todo: enabling this seems to make some locations unreachable. for now, disable it...
    # set_rule(self.get_entrance("F9-F9b"), lambda state: state.has("Opened gate (SH)", p))
    set_rule(self.get_entrance("F9b-F9"), lambda state: state.has("Opened gate (SH)", p))

    # 6Db switch
    region = self.get_region("6Db")
    loc = Location(p, "6Db: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (WL)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("6D-6Db"), lambda state: state.has("Opened gate (WL)", p))
    set_rule(self.get_entrance("6Db-6D"), lambda state: state.has("Opened gate (WL)", p))

    # todo: E8-E8b needs (rahab + PM + skeleton ape) or (rahab + bone ark)
    set_rule(self.get_entrance("E8-E8b"), lambda state: state.has("Rahab soul", p))

    # 5Db switch
    region = self.get_region("5Db")
    loc = Location(p, "5Db: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (WL 2)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("5D-5Db"), lambda state: state.has("Opened gate (WL 2)", p))
    set_rule(self.get_entrance("5Db-5D"), lambda state: state.has("Opened gate (WL 2)", p))

    # 0E switch
    region = self.get_region("0E")
    loc = Location(p, "0E: Dynamite Switch", None, region)
    loc.place_locked_item(Item("Opened floor (TLV)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("0E-0D"), lambda state: state.has("Opened floor (TLV)", p) and
                                                       state.has_group("height", p))
    set_rule(self.get_entrance("0D-0E"), lambda state: state.has("Opened floor (TLV)", p))

    # 06 switch
    region = self.get_region("06")
    loc = Location(p, "06: Dynamite Switch", None, region)
    loc.place_locked_item(Item("Opened floor (TLV 2)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("06-1A"), lambda state: state.has("Opened floor (TLV 2)", p) and
                                                       state.has_group("height", p))
    set_rule(self.get_entrance("1A-06"), lambda state: state.has("Opened floor (TLV 2)", p))

    # 49 switch
    region = self.get_region("49")
    loc = Location(p, "49: Gate Switch", None, region)
    loc.place_locked_item(Item("Opened gate (DGH)", ItemClassification.filler, None, p)) # todo: filler?
    region.locations.append(loc)
    set_rule(self.get_entrance("49-4A"), lambda state: state.has("Opened gate (DGH)", p))
    set_rule(self.get_entrance("4A-49"), lambda state: state.has("Opened gate (DGH)", p))

    # 90 mina event
    region = self.get_region("90")
    loc = Location(p, "90: Mina doppelganger event", None, region)
    loc.place_locked_item(Item("Mina doppelganger event", ItemClassification.progression, None, p))
    region.locations.append(loc)
    set_rule(loc, lambda state: state.has("Mina's Talisman", p))
    set_rule(self.get_entrance("CC-D8"), lambda state: state.has("Mina doppelganger event", p))

    region = self.get_region("15D")
    loc = Location(p, "15D: Defeat Menace", None, region)
    loc.place_locked_item(Item("Victory", ItemClassification.progression, None, p))
    region.locations.append(loc)
    self.multiworld.completion_condition[p] = lambda state: state.has("Victory", p)

    # visualize_regions(self.multiworld.get_region("Menu", p), "my_world.puml")
