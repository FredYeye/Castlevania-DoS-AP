from BaseClasses import Region
from .locations import location_table

def create_regions(self) -> None:
    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    main_region = Region("Main area", self.player, self.multiworld)
    main_region.add_locations(self.location_name_to_id, None)
    self.multiworld.regions.append(main_region)

    final_region = Region("Final area", self.player, self.multiworld)
    self.multiworld.regions.append(final_region)

    menu_region.connect(main_region)
    main_region.connect(final_region)
