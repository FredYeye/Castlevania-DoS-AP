from BaseClasses import Region
from .locations import *

def create_regions(self) -> None:
    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    lv01_region = Region("LV01", self.player, self.multiworld)
    self.multiworld.regions.append(lv01_region)
    lv01_region_locs = {k: self.location_name_to_id[k] for k in loc_lv01}
    lv01_region.add_locations(lv01_region_locs)

    main_region = Region("Main area", self.player, self.multiworld)
    main_region_locs = {k: self.location_name_to_id[k] for k in loc_others}
    main_region.add_locations(main_region_locs, None)
    self.multiworld.regions.append(main_region)

    final_region = Region("Final area", self.player, self.multiworld)
    self.multiworld.regions.append(final_region)

    menu_region.connect(lv01_region)
    lv01_region.add_exits({"Main area": "Flying Armor exit"}, {"Main area": lambda state: state.has_group("long_jump", self.player)})
    lv01_region.add_exits({"Main area": "Drawbridge exit"}, {"Main area": lambda state: state.has_group("high_jump", self.player)})
    main_region.connect(final_region)
