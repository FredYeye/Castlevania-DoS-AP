import os
from .locations import *
from .items import *

# patch format:
# if item      (6 bytes): 0x01, map_lo, map_hi, enm_slot, item/soul type, item/soul id)
# if boss drop (4 bytes): 0x02, boss id, item/soul type, item/soul id)

def patch(self, output_directory: str) -> None:
    filename = f"{self.multiworld.get_out_file_name_base(self.player)}.patch"

    patch_data = bytearray()

    for k in self.get_locations():
        if k.address != None:
            match location_table[k.name]:
                case StaticItem(map_id, enm_slot):
                    map_id_hi = map_id >> 8
                    map_id_lo = map_id & 0xFF
                    patch_data.extend([0x01, map_id_lo, map_id_hi, enm_slot])
                case Boss(id):
                    patch_data.extend([0x02, id])

            if item_table[k.item.name].is_soul == False:
                patch_data.extend([0x11])
            else:
                patch_data.extend([0x12])
            
            patch_data.extend([item_table[k.item.name].item_id])

    with open(os.path.join(output_directory, filename), 'wb') as f:
        f.write(patch_data)
