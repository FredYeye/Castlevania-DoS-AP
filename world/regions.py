from BaseClasses import Region
from .locations import *
from typing import List, Optional
from dataclasses import dataclass

# todo: probably remove this class? or... somehow add rules to it...
@dataclass
class Entr():
    destination: str
    extra_id: str = "" # in case there are more entrances to the same map

@dataclass(frozen=True)
class Map():
    connections: List[Entr]
    locations: Optional[List[str]] = None

maps: dict[str, Map] = {
    "01" : Map([Entr("05")]),
    "02" : Map([Entr("05")]),
    "03" : Map([Entr("1A", "upper"), Entr("1A", "lower"), Entr("1C")], loc_03),
    "04" : Map([Entr("1A")]),
    "05" : Map([Entr("01"), Entr("02"), Entr("08")]),
    "08" : Map([Entr("05"), Entr("0F")]),
    "09" : Map([Entr("0C"), Entr("1A")], loc_09),
    "0A" : Map([Entr("0D"), Entr("1A")]),
    "0B" : Map([Entr("1A")]),
    "0C" : Map([Entr("09"), Entr("0F")], loc_0C),
    "0D" : Map([Entr("0A"), Entr("10"), Entr("1B")], loc_0D),
    "0F" : Map([Entr("08"), Entr("0C"), Entr("11"), Entr("18")], loc_0F),
    "10" : Map([Entr("0D"), Entr("13")]),
    "11" : Map([Entr("0F"), Entr("16")]),
    "12" : Map([Entr("1B")], loc_12),
    "13" : Map([Entr("10"), Entr("15")]),
    "14" : Map([Entr("1B")], loc_14),
    "15" : Map([Entr("13"), Entr("16")]),
    "16" : Map([Entr("11"), Entr("15"), Entr("16b"), Entr("7E")]),
    "16b" : Map([Entr("16"), Entr("17")]), # drawbridge switch
    "17" : Map([Entr("16b"), Entr("58")]),
    "18" : Map([Entr("0F")]),
    "1A" : Map([Entr("03", "upper"), Entr("03", "lower"), Entr("04"), Entr("09"), Entr("0A"), Entr("0B")], loc_1A),
    "1B" : Map([Entr("0D"), Entr("12"), Entr("14")]),
    "1C" : Map([Entr("03")]),
    "47" : Map([Entr("4D"), Entr("58")]),
    "4D" : Map([Entr("47"), Entr("9D")]),
    "58" : Map([Entr("17"), Entr("47")]),
    "5D" : Map([Entr("5E")], loc_5D),
    "5E" : Map([Entr("5D"), Entr("60"), Entr("61")]),
    "5F" : Map([Entr("64"), Entr("5E")]),
    "60" : Map([Entr("5E"), Entr("65")]),
    "61" : Map([Entr("5E"), Entr("62"), Entr("65")]),
    "62" : Map([Entr("61"), Entr("66")]),
    "63" : Map([Entr("6E")], loc_63),
    "64" : Map([Entr("5F"), Entr("67"), Entr("68"), Entr("7E"), Entr("7F")], loc_64),
    "65" : Map([Entr("60"), Entr("61"), Entr("69"), Entr("6A"), Entr("81")]),
    "66" : Map([Entr("62"), Entr("6A"), Entr("6B")]),
    "67" : Map([Entr("64"), Entr("70")]),
    "68" : Map([Entr("64")], loc_68),
    "69" : Map([Entr("65"), Entr("6C")]),
    "6A" : Map([Entr("66")]),
    "6B" : Map([Entr("66"), Entr("6E")]),
    "6C" : Map([Entr("69"), Entr("71"), Entr("72")]),
    "6E" : Map([Entr("63"), Entr("80")]),
    "6F" : Map([Entr("70")], loc_6F),
    "70" : Map([Entr("67"), Entr("6F")]),
    "71" : Map([Entr("6C")], loc_71),
    "72" : Map([Entr("6C"), Entr("9F")]),
    "7E" : Map([Entr("16"), Entr("64")]),
    "7F" : Map([Entr("64")]),
    "80" : Map([Entr("6E")]),
    "81" : Map([Entr("65")]),
    "82" : Map([Entr("84"), Entr("89"), Entr("8A"), Entr("9D")], loc_82),
    "82b" : Map([Entr("83")], loc_82b), # upper area
    "83" : Map([Entr("82b"), Entr("89")]),
    "84" : Map([Entr("82"), Entr("85")]),
    "85" : Map([Entr("8B"), Entr("84"), Entr("A5")], loc_85),
    "89" : Map([Entr("82"), Entr("83"), Entr("A6", "lower"), Entr("A6", "upper")]),
    "8A" : Map([Entr("82")]),
    "8B" : Map([Entr("85"), Entr("91"), Entr("9F"), Entr("A3")]),
    "91" : Map([Entr("8B")]),
    "93" : Map([Entr("98"), Entr("A6")]),
    "94" : Map([Entr("98")]),
    "98" : Map([Entr("93"), Entr("94"), Entr("9B"), Entr("A2")]),
    "99" : Map([Entr("9B")]),
    "9B" : Map([Entr("98"), Entr("99"), Entr("9C")]),
    "9C" : Map([Entr("9B")], loc_9C),
    "9D" : Map([Entr("4D"), Entr("82")]),
    "9F" : Map([Entr("72"), Entr("8B")]),
    "A2" : Map([Entr("98"), Entr("AA")]),
    "A3" : Map([Entr("8B")]),
    "A5" : Map([Entr("84")]),
    "A6" : Map([Entr("89", "lower"), Entr("89", "upper"), Entr("93")], loc_A6),
    "AA" : Map([Entr("A2"), Entr("BF")]),
    "BF" : Map([Entr("AA")]),
}

def create_regions(self) -> None:
    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    regions: List[Region] = []
    for map_name, map_data in maps.items():
        region = Region(map_name, self.player, self.multiworld)
        regions.append(region)
        self.multiworld.regions.append(region)
        if map_data.locations != None:
            for loc in map_data.locations:
                asd = Location(self.player, loc, self.location_name_to_id[loc], region)
                region.locations.append(asd)

    for region in regions:
        for connection in maps[region.name].connections:
            region.add_exits({connection.destination: region.name + "-" + connection.destination + connection.extra_id})

    menu_region.add_exits({"02": "asd"}, None)
