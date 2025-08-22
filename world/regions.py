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
    "01" : Map([Entr("05")], loc_01),
    "02" : Map([Entr("05")]),
    "03" : Map([Entr("1A", "upper"), Entr("1A", "lower"), Entr("1C")], loc_03),
    "04" : Map([Entr("1A")]),
    "05" : Map([Entr("02"), Entr("05b"), Entr("08")]),
    "05b" : Map([Entr("01"), Entr("05")]), # upper area
    "08" : Map([Entr("05"), Entr("08b"), Entr("0F")]),
    "08b" : Map([Entr("08"), Entr("57")], loc_08b), # upper area
    "09" : Map([Entr("09b"), Entr("0C")]),
    "09b": Map([Entr("09"), Entr("1A")], loc_09b),
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
    "16" : Map([Entr("11"), Entr("15"), Entr("16b"), Entr("7E")], loc_16),
    "16b" : Map([Entr("16"), Entr("17")]), # drawbridge switch side
    "17" : Map([Entr("16b"), Entr("58")]),
    "18" : Map([Entr("0F")]),
    # "19" : Map([Entr("1A")]), lost village warp, opens after finding another warp
    "1A" : Map([Entr("03", "upper"), Entr("03", "lower"), Entr("04"), Entr("09"), Entr("0A"), Entr("0B")], loc_1A),
    "1B" : Map([Entr("0D"), Entr("12"), Entr("14")]),
    "1C" : Map([Entr("03")]),
    "1D" : Map([Entr("1E")], loc_1D),
    "1E" : Map([Entr("1D"), Entr("1F")]),
    "1F" : Map([Entr("1E"), Entr("26")]),
    "20" : Map([Entr("26"), Entr("38")]),
    "21" : Map([Entr("57")]), # todo: connect with 27?
    "23" : Map([Entr("3E")], loc_23),
    "24" : Map([Entr("3A")], loc_24),
    "25" : Map([Entr("3A"), Entr("3B")]),
    "26" : Map([Entr("1F"), Entr("20"), Entr("3C")]),

    # sliding rooms with items
    "27" : Map([Entr("38")], loc_27),
    "2B" : Map([Entr("38")], loc_2B),
    "2E" : Map([Entr("38")], loc_2E),
    "2F" : Map([Entr("38")], loc_2F),
    "32" : Map([Entr("38")], loc_32),

    "37" : Map([Entr("38")], loc_37),

    # 38: sliding rooms entrance. ignore most individual rooms for now and connect stuff directly to 38.
    # maybe make an event here or w/e
    "38" : Map([Entr("20"), Entr("21"), Entr("27"), Entr("2B"), Entr("2E"), Entr("2F"), Entr("32"), Entr("37"), Entr("46")]),
    "3A" : Map([Entr("24"), Entr("25"), Entr("3E"), Entr("40")]),
    "3B" : Map([Entr("25"), Entr("41"), Entr("42"), Entr("5B")]),
    "3C" : Map([Entr("26"), Entr("42"), Entr("43")]),
    "3E" : Map([Entr("23"), Entr("3A"), Entr("59")]),
    "40" : Map([Entr("3A")], loc_40),
    "41" : Map([Entr("3A"), Entr("3B")]),
    "42" : Map([Entr("3B"), Entr("3C"), Entr("43b"), Entr("45b")]),
    "43" : Map([Entr("3C")]),
    "43b" : Map([Entr("42")], loc_43b),
    "45" : Map([Entr("45b"), Entr("4A")]),
    "45b" : Map([Entr("42"), Entr("45")]), # left side
    "46" : Map([Entr("38"), Entr("4B")]),
    "47" : Map([Entr("4D"), Entr("58")]),
    "4A" : Map([Entr("45"), Entr("4B"), Entr("51"), Entr("52"), Entr("53")]),
    "4B" : Map([Entr("46"), Entr("4A"), Entr("4Cb"), Entr("54"), Entr("55"), Entr("5A")]),
    "4C" : Map([Entr("4Cb"), Entr("4D")], loc_4C),
    "4Cb" : Map([Entr("4B"), Entr("4C")]), # left side
    "4D" : Map([Entr("47"), Entr("4C"), Entr("9D")]),
    "51" : Map([Entr("4A")]),
    "52" : Map([Entr("4A")], loc_52),
    "53" : Map([Entr("4A")]),
    "54" : Map([Entr("4B"), Entr("5C")]), # loc_54 todo: mina's talisman
    "55" : Map([Entr("4B")]),
    "57" : Map([Entr("08b"), Entr("21")]),
    "58" : Map([Entr("17"), Entr("47")]),
    "59" : Map([Entr("3E")]),
    "5A" : Map([Entr("4B")]),
    "5B" : Map([Entr("3B")]),
    "5C" : Map([Entr("54"), Entr("9E")]),
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
    "83" : Map([Entr("82b"), Entr("83b"), Entr("89")]),
    "83b" : Map([Entr("83"), Entr("88")], loc_83b), # upper area
    "84" : Map([Entr("82"), Entr("85")]),
    "85" : Map([Entr("8B"), Entr("84"), Entr("A5")], loc_85),
    "87" : Map([Entr("8C"), Entr("8D"), Entr("9E")]),
    "88" : Map([Entr("83"), Entr("8F")]),
    "89" : Map([Entr("82"), Entr("83"), Entr("A6", "lower"), Entr("A6", "upper")]),
    "8A" : Map([Entr("82")]),
    "8B" : Map([Entr("85"), Entr("91"), Entr("9F"), Entr("A3")]),
    "8C" : Map([Entr("87")]),
    "8D" : Map([Entr("87"), Entr("8E")]),
    "8E" : Map([Entr("8D"), Entr("8F")]),
    "8F" : Map([Entr("88"), Entr("8E"), Entr("A4")]),
    "91" : Map([Entr("8B"), Entr("91b")]),
    "91b" : Map([Entr("91"), Entr("95")]), # right side
    "93" : Map([Entr("98"), Entr("A6")]),
    "94" : Map([Entr("98")]),
    "95" : Map([Entr("91b"), Entr("99b"), Entr("9A"), Entr("A1")]),
    "98" : Map([Entr("93"), Entr("94"), Entr("9B"), Entr("A2")]),
    "99" : Map([Entr("99b"), Entr("9B")]),
    "99b" : Map([Entr("95"), Entr("99")]), # left side
    "9A" : Map([Entr("95")], loc_9A),
    "9B" : Map([Entr("98"), Entr("99"), Entr("9C")]),
    "9C" : Map([Entr("9B")], loc_9C),
    "9D" : Map([Entr("4D"), Entr("82")]),
    "9E" : Map([Entr("5C"), Entr("87")]),
    "9F" : Map([Entr("72"), Entr("8B")]),
    "A1" : Map([Entr("95"), Entr("F6")]),
    "A2" : Map([Entr("98"), Entr("AA")]),
    "A3" : Map([Entr("8B")]),
    "A4" : Map([Entr("8F")]),
    "A5" : Map([Entr("84")]),
    "A6" : Map([Entr("89", "lower"), Entr("89", "upper"), Entr("93")], loc_A6),
    "A7" : Map([Entr("AD")], loc_A7),
    "A8" : Map([Entr("A9"), Entr("B1")], loc_A8),
    "A9" : Map([Entr("A8"), Entr("B2")]),
    "AA" : Map([Entr("A2"), Entr("B3"), Entr("BF")], loc_AA),
    "AB" : Map([Entr("AE")]),
    "AC" : Map([Entr("AE")], loc_AC),
    "AD" : Map([Entr("A7"), Entr("AE"), Entr("AF"), Entr("B0")]),
    "AE" : Map([Entr("AB"), Entr("AC"), Entr("AD"), Entr("B4")]),
    "AF" : Map([Entr("AD"), Entr("AFb")]),
    "AFb" : Map([Entr("AF"), Entr("105")]), # right side
    "B0" : Map([Entr("AD"), Entr("B8")]),
    "B1" : Map([Entr("A8"), Entr("B5"), Entr("B7"), Entr("BD")]),
    "B2" : Map([Entr("A9"), Entr("BB")]),
    "B3" : Map([Entr("AA"), Entr("BB")]),
    "B4" : Map([Entr("AE"), Entr("BB")]),
    "B5" : Map([Entr("B1"), Entr("B9")]),
    "B6" : Map([Entr("BA")], loc_B6),
    "B7" : Map([Entr("B1"), Entr("BA")]),
    "B8" : Map([Entr("B0")], loc_B8),
    "B9" : Map([Entr("B5"), Entr("B9b")], loc_B9),
    "B9b" : Map([Entr("B9"), Entr("BCb")]),
    "BA" : Map([Entr("B6"), Entr("B7")], loc_BA),
    "BB" : Map([Entr("B2"), Entr("B3"), Entr("B4"), Entr("BC"), Entr("BE")], loc_BB),
    "BC" : Map([Entr("BB"), Entr("BCb")]),
    "BCb" : Map([Entr("B9b"), Entr("BC"), Entr("DA")], loc_BCb),
    "BD" : Map([Entr("B1")]),
    "BE" : Map([Entr("BB")]),
    "BF" : Map([Entr("AA")]),
    "C0" : Map([Entr("C3")]), # todo: event connection
    "C1" : Map([Entr("C6"), Entr("DA")]),
    "C3" : Map([Entr("C0"), Entr("C7f"), Entr("C7g")], loc_C3),
    "C4" : Map([Entr("C7d"), Entr("C4b")]),
    "C4b" : Map([Entr("C4"), Entr("C7e")], loc_C4b),
    "C5" : Map([Entr("C7b"), Entr("C7c")]),
    "C6" : Map([Entr("C1"), Entr("C7")]), # todo: item

    # tower
    "C7" : Map([Entr("C6"), Entr("CB")]),
    "C7b" : Map([Entr("C5"), Entr("CB")]), # 2nd floor
    "C7c" : Map([Entr("C5"), Entr("CA")]), # 3rd floor
    "C7d" : Map([Entr("C4"), Entr("CA")]),
    "C7e" : Map([Entr("C4b"), Entr("C9")]),
    "C7f" : Map([Entr("C9"), Entr("C3")]),
    "C7g" : Map([Entr("C3"), Entr("C8")]),
    "C7h" : Map([Entr("C8b")]),

    "C8" : Map([Entr("C7g"), Entr("C8b")]),
    "C8b" : Map([Entr("C7h"), Entr("C8"), Entr("DC")]),
    "C9" : Map([Entr("C7e"), Entr("C7f")]),
    "CA" : Map([Entr("C7c"), Entr("C7d")]),
    "CB" : Map([Entr("C7"), Entr("C7b"), Entr("CC")], loc_CB),
    "CC" : Map([Entr("CB")]),
    "DA" : Map([Entr("BCb"), Entr("C1")]),
    "DC" : Map([Entr("C8")]),
    "E8" : Map([Entr("EB")]),
    "EA" : Map([Entr("ECb")], loc_EA),
    "EB" : Map([Entr("E8"), Entr("ECd")]),
    "EC"  : Map([Entr("EA"), Entr("ECb"), Entr("ED")]), # upper entrance
    "ECb" : Map([Entr("ECc")], loc_ECb), # middle area
    "ECc" : Map([Entr("ECb"), Entr("ED")], loc_ECc), # lower entrance
    "ECd" : Map([Entr("EB"), Entr("ECc"), Entr("EE")]), # bottom area
    "ED" : Map([Entr("ECc"), Entr("EC"), Entr("EF"), Entr("106")]),
    "EE" : Map([Entr("ECd"), Entr("103")]),
    "EF" : Map([Entr("ED"), Entr("F1")]),
    "F0" : Map([Entr("F8b")]), # todo: rock prize game
    "F1" : Map([Entr("EF"), Entr("F2")], loc_F1),
    "F2" : Map([Entr("F1"), Entr("F3"), Entr("108")]),
    "F3" : Map([Entr("F2"), Entr("F4"), Entr("F7")]),
    "F4" : Map([Entr("F3"), Entr("F5")]),
    "F5" : Map([Entr("F4"), Entr("F6"), Entr("109")], loc_F5),
    "F6" : Map([Entr("F5"), Entr("A1")]),
    "F7" : Map([Entr("F3"), Entr("F8b")]),
    "F8" : Map([Entr("F8b"), Entr("F9"), Entr("FA")]),
    "F8b" : Map([Entr("F0"), Entr("F7")]), # upper area
    "F9" : Map([Entr("F8")]),
    "FA" : Map([Entr("F8"), Entr("FD")]),
    "FB" : Map([Entr("FC"), Entr("105"), Entr("107")]),
    "FC" : Map([Entr("FB"), Entr("FE")]),
    "FD" : Map([Entr("FA"), Entr("FF")]),
    "FE" : Map([Entr("FC"), Entr("100")], loc_FE),
    "FF" : Map([Entr("FD"), Entr("100")], loc_FF),
    "100" : Map([Entr("FE"), Entr("FF")]),
    "103" : Map([Entr("EE"), Entr("10A")]),
    "105" : Map([Entr("AFb"), Entr("FB")]),
    "106" : Map([Entr("ED")]),
    "107" : Map([Entr("FB")]),
    "108" : Map([Entr("F2")]),
    "109" : Map([Entr("F5")]),
    "10A" : Map([Entr("103")]), # todo: needs zephyr
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
                loc_data = Location(self.player, loc, self.location_name_to_id[loc], region)
                region.locations.append(loc_data)

    for region in regions:
        for connection in maps[region.name].connections:
            region.add_exits({connection.destination: region.name + "-" + connection.destination + connection.extra_id})

    menu_region.add_exits({"02": "asd"}, None)
