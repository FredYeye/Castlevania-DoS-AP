from enum import Enum
from BaseClasses import Region
from .locations import *
from typing import List, Optional
from dataclasses import dataclass

class EntrReq(Enum):
    HEIGHT = 0
    MEDIUM_HEIGHT = 1
    BIG_HEIGHT = 2
    HEIGHT_AND_DISTANCE = 3
    DISTANCE = 4
    BALORE = 5
    MAGIC_SEAL_2 = 6
    MAGIC_SEAL_3 = 7
    MAGIC_SEAL_4 = 8
    MAGIC_SEAL_5 = 9
    SMALL = 10
    RAHAB = 11
    ZEPHYR = 12
    BIGGER_HEIGHT = 13 # todo: name? lol
    BALORE_OR_MEDIUM_HEIGHT = 14
    RAHAB_OR_HEIGHT = 15
    RAHAB_AND_HEIGHT = 16
    FLIGHT = 17
    MAGIC_SEAL_5_AND_HEIGHT = 18,

@dataclass
class Entr():
    destination: str
    extra_id: str = "" # in case there are more entrances to the same map
    req: Optional[EntrReq] = None

@dataclass(frozen=True)
class Map():
    connections: List[Entr]
    locations: Optional[List[str]] = None

maps: dict[str, Map] = {
    "01" : Map([Entr("05")], loc_01),
    "02" : Map([Entr("05")]),
    "03" : Map([Entr("1A", "upper"), Entr("1A", "lower"), Entr("1C")], loc_03),
    "04" : Map([Entr("1A")]),
    "05" : Map([Entr("02"), Entr("05b", req=EntrReq.BIG_HEIGHT), Entr("08")]),
    "05b" : Map([Entr("01"), Entr("05")]), # upper area
    "06" : Map([Entr("06b"), Entr("1A")]), # upper area
    "06b" : Map([Entr("06", req=EntrReq.HEIGHT), Entr("07")]), # lower area
    "07" : Map([Entr("06b"), Entr("0E")], loc_07),
    "08" : Map([Entr("05"), Entr("08b", req=EntrReq.HEIGHT_AND_DISTANCE), Entr("0F")]),
    "08b" : Map([Entr("08"), Entr("57")], loc_08b), # upper area

    # todo: nothing is actually required. a precise backdash jump clears the gap.
    # lago's rando modifies the layout so nothing is required. might be a good option
    # "09" : Map([Entr("09b", req=EntrReq.DISTANCE), Entr("0C")]),
    "09" : Map([Entr("09b"), Entr("0C")]),
    "09b": Map([Entr("09"), Entr("1A")], loc_09b),
    "0A" : Map([Entr("0D"), Entr("1A")]),
    "0B" : Map([Entr("1A")]),
    "0C" : Map([Entr("09"), Entr("0F")], loc_0C),
    "0D" : Map([Entr("0A"), Entr("0E"), Entr("10", req=EntrReq.DISTANCE), Entr("1B")], loc_0D),
    "0E" : Map([Entr("07"), Entr("0D"), Entr("0Eb")], loc_0E), # upper level
    "0Eb" : Map([Entr("0E", req=EntrReq.HEIGHT), Entr("0Ec"), Entr("7C")]), # middle level
    "0Ec" : Map([Entr("0Eb", req=EntrReq.HEIGHT), Entr("7D")]), # bottom level
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
    # "19" : Map([Entr("1A")]), # todo: lost village warp, opens after finding another warp
    "1A" : Map([Entr("03", "upper"), Entr("03", "lower"), Entr("04"), Entr("06"), Entr("09"), Entr("0A"), Entr("0B")], loc_1A),
    "1B" : Map([Entr("0D"), Entr("12"), Entr("14")]),
    "1C" : Map([Entr("03")]),
    "1D" : Map([Entr("1E")], loc_1D),
    "1E" : Map([Entr("1D", req=EntrReq.MEDIUM_HEIGHT), Entr("1F")]),
    "1F" : Map([Entr("1E"), Entr("26")]),
    "20" : Map([Entr("26", req=EntrReq.HEIGHT), Entr("38")]),
    "21" : Map([Entr("27"), Entr("57")]), # the left entrance to the sliding rooms, connects to the cestus room
    "22" : Map([Entr("39")], loc_22),
    "23" : Map([Entr("3E")], loc_23),
    "24" : Map([Entr("3A")], loc_24),
    "25" : Map([Entr("3A"), Entr("3B")]),
    "26" : Map([Entr("1F", req=EntrReq.DISTANCE), Entr("20"), Entr("3C")]),

    # sliding rooms with items
    "27" : Map([Entr("38")], loc_27),
    "2B" : Map([Entr("38")], loc_2B),
    "2E" : Map([Entr("38")], loc_2E),
    "2F" : Map([Entr("38")], loc_2F),
    "32" : Map([Entr("38")], loc_32),

    "37" : Map([Entr("38")], loc_37),

    # 38: sliding rooms entrance. ignore most individual rooms for now and connect stuff directly to 38.
    # maybe make an event here or w/e
    "38" : Map([Entr("20", req=EntrReq.HEIGHT), Entr("21", req=EntrReq.HEIGHT), Entr("27"), Entr("2B"), Entr("2E", req=EntrReq.HEIGHT), Entr("2F", req=EntrReq.HEIGHT), Entr("32", req=EntrReq.HEIGHT), Entr("37", req=EntrReq.HEIGHT), Entr("46")]),
    "39" : Map([Entr("22"), Entr("3D")], loc_39),
    "3A" : Map([Entr("24"), Entr("25"), Entr("3E", req=EntrReq.MEDIUM_HEIGHT), Entr("40")]),
    "3B" : Map([Entr("25"), Entr("41"), Entr("42"), Entr("5B")]),
    "3C" : Map([Entr("26"), Entr("42"), Entr("43")]),
    "3D" : Map([Entr("39"), Entr("3F")], loc_3D),
    "3E" : Map([Entr("23", req=EntrReq.MAGIC_SEAL_3), Entr("3A"), Entr("59")]),
    "3F" : Map([Entr("3D", req=EntrReq.MAGIC_SEAL_4), Entr("44")]),
    "40" : Map([Entr("3A")], loc_40),
    "41" : Map([Entr("3A", req=EntrReq.HEIGHT), Entr("3B")]),
    "42" : Map([Entr("3B", req=EntrReq.DISTANCE), Entr("3C"), Entr("43b"), Entr("45b")]),
    "43" : Map([Entr("3C")]),
    "43b" : Map([Entr("42", req=EntrReq.MEDIUM_HEIGHT)], loc_43b),
    "44" : Map([Entr("3F"), Entr("49")]), # todo: blocked by 3 soul walls
    "45" : Map([Entr("45b", req=EntrReq.SMALL), Entr("4A")]),
    "45b" : Map([Entr("42"), Entr("45", req=EntrReq.SMALL)]), # left side
    "46" : Map([Entr("38"), Entr("4B")]),
    "47" : Map([Entr("4D"), Entr("58")]),
    "48" : Map([Entr("49")]),
    "49" : Map([Entr("44"), Entr("48"), Entr("4A"), Entr("4E"), Entr("4F"), Entr("50")]),
    "4A" : Map([Entr("45"), Entr("49"), Entr("4B"), Entr("51"), Entr("52"), Entr("53")]),
    "4B" : Map([Entr("46"), Entr("4A"), Entr("4Cb"), Entr("54"), Entr("55"), Entr("5A")]),
    "4C" : Map([Entr("4Cb", req=EntrReq.SMALL), Entr("4D")], loc_4C),
    "4Cb" : Map([Entr("4B", req=EntrReq.HEIGHT), Entr("4C", req=EntrReq.SMALL)]), # left side
    "4D" : Map([Entr("47"), Entr("4C", req=EntrReq.HEIGHT), Entr("9D")]),
    "4E" : Map([Entr("49")]),
    "4F" : Map([Entr("49")]),
    "50" : Map([Entr("49"), Entr("158")]),
    "51" : Map([Entr("4A")]),
    "52" : Map([Entr("4A")], loc_52),
    "53" : Map([Entr("4A")]),
    "54" : Map([Entr("4B"), Entr("5C")], loc_54),
    "55" : Map([Entr("4B")]),
    "56" : Map([Entr("5C")], loc_56),
    "57" : Map([Entr("08b"), Entr("21")]),
    "58" : Map([Entr("17"), Entr("47")]),
    "59" : Map([Entr("3E")]),
    "5A" : Map([Entr("4B")]),
    "5B" : Map([Entr("3B")]),
    "5C" : Map([Entr("54"), Entr("56", req=EntrReq.BIGGER_HEIGHT), Entr("9E")]),
    "5D" : Map([Entr("5Db"), Entr("5E")], loc_5D),
    "5Db" : Map([Entr("5D")], loc_5Db),
    "5E" : Map([Entr("5D"), Entr("60"), Entr("61")]),
    "5F" : Map([Entr("64"), Entr("5E")]),
    "60" : Map([Entr("5E"), Entr("65")]),
    "61" : Map([Entr("5E"), Entr("62"), Entr("65")]),
    "62" : Map([Entr("61"), Entr("66")]),
    "63" : Map([Entr("6E")], loc_63),
    "64" : Map([Entr("5F"), Entr("67"), Entr("68"), Entr("7E"), Entr("7F")], loc_64),
    "65" : Map([Entr("60"), Entr("61"), Entr("69"), Entr("6A"), Entr("81")]),
    "66" : Map([Entr("62"), Entr("6A"), Entr("6B")]),
    "67" : Map([Entr("64", req=EntrReq.BALORE), Entr("70", req=EntrReq.BALORE)]),
    "68" : Map([Entr("64")], loc_68),
    "69" : Map([Entr("65"), Entr("6C")]),
    "6A" : Map([Entr("66"), Entr("6D")]),
    "6B" : Map([Entr("66"), Entr("6E")]),

    # todo: 71 can also be entered with bat + overhead attack
    "6C" : Map([Entr("69"), Entr("71", req=EntrReq.BALORE), Entr("72", req=EntrReq.BALORE_OR_MEDIUM_HEIGHT)]),
    "6D" : Map([Entr("6A"), Entr("6Db")]),
    "6Db" : Map([Entr("6D"), Entr("102")], loc_6Db), # right side
    "6E" : Map([Entr("63"), Entr("80")]),
    "6F" : Map([Entr("70")], loc_6F),
    "70" : Map([Entr("67", req=EntrReq.BALORE), Entr("6F", req=EntrReq.BALORE)]),
    "71" : Map([Entr("6C")], loc_71),
    "72" : Map([Entr("6C"), Entr("9F")]),
    "73" : Map([Entr("74")], loc_73),
    "74" : Map([Entr("73", req=EntrReq.RAHAB), Entr("76", req=EntrReq.RAHAB)]),
    "75" : Map([Entr("77"), Entr("7D")]),
    "76" : Map([Entr("74"), Entr("77", req=EntrReq.HEIGHT)]),
    "77" : Map([Entr("75", req=EntrReq.BIG_HEIGHT), Entr("76"), Entr("78")]),
    "78" : Map([Entr("77"), Entr("79")]),
    "79" : Map([Entr("78", req=EntrReq.RAHAB), Entr("7A", req=EntrReq.RAHAB)], loc_79),
    "7A" : Map([Entr("79"), Entr("7B")]),
    "7B" : Map([Entr("7A", req=EntrReq.RAHAB), Entr("101", req=EntrReq.RAHAB)], loc_7B),
    "7C" : Map([Entr("0Eb"), Entr("5Db")]),
    "7D" : Map([Entr("0Ec"), Entr("75")]),
    "7E" : Map([Entr("16"), Entr("64")]),
    "7F" : Map([Entr("64")]),
    "80" : Map([Entr("6E")]),
    "81" : Map([Entr("65")]),
    "82" : Map([Entr("84"), Entr("89"), Entr("8A"), Entr("9D")], loc_82),
    "82b" : Map([Entr("83")], loc_82b), # upper area
    "83" : Map([Entr("82b"), Entr("83b", req=EntrReq.HEIGHT), Entr("89")]),
    "83b" : Map([Entr("83"), Entr("86", req=EntrReq.BIGGER_HEIGHT), Entr("88")], loc_83b), # upper area
    "84" : Map([Entr("82"), Entr("85")]),
    "85" : Map([Entr("8B"), Entr("84"), Entr("A5")], loc_85),
    "86" : Map([Entr("83b")], loc_86),
    "87" : Map([Entr("8C"), Entr("8D"), Entr("9E")]),
    "88" : Map([Entr("83"), Entr("8F")]),
    "89" : Map([Entr("82"), Entr("83"), Entr("A6", "lower"), Entr("A6", "upper")]),
    "8A" : Map([Entr("82"), Entr("90", req=EntrReq.MAGIC_SEAL_5)]),
    "8B" : Map([Entr("85"), Entr("91"), Entr("9F"), Entr("A3")]),
    "8C" : Map([Entr("87"), Entr("8Cb")]),
    "8Cb" : Map([Entr("8C"), Entr("92")]),
    "8D" : Map([Entr("87"), Entr("8E")]),
    "8E" : Map([Entr("8D", req=EntrReq.MAGIC_SEAL_2), Entr("8F")]),
    "8F" : Map([Entr("88"), Entr("8E", req=EntrReq.HEIGHT), Entr("A4")]),
    "90" : Map([Entr("8A"), Entr("94")]),
    "91" : Map([Entr("8B"), Entr("91b", req=EntrReq.RAHAB)]),
    "91b" : Map([Entr("91", req=EntrReq.RAHAB), Entr("95")]), # right side
    "92" : Map([Entr("8Cb"), Entr("96"), Entr("A0")]),
    "93" : Map([Entr("98"), Entr("A6")]),
    "94" : Map([Entr("90", req=EntrReq.MAGIC_SEAL_5), Entr("98")]),
    "95" : Map([Entr("91b"), Entr("99b"), Entr("9A"), Entr("A1")]),
    "96" : Map([Entr("92"), Entr("97")]),
    "97" : Map([Entr("96", req=EntrReq.HEIGHT), Entr("98b")]),
    "98" : Map([Entr("93"), Entr("94"), Entr("9B"), Entr("A2")]),
    "98b" : Map([Entr("97")], loc_98b),
    "99" : Map([Entr("99b", req=EntrReq.RAHAB), Entr("9B")]),
    "99b" : Map([Entr("95"), Entr("99", req=EntrReq.RAHAB)]), # left side
    "9A" : Map([Entr("95")], loc_9A),
    "9B" : Map([Entr("98"), Entr("99"), Entr("9C")]),
    "9C" : Map([Entr("9B")], loc_9C),
    "9D" : Map([Entr("4D"), Entr("82")]),
    "9E" : Map([Entr("5C"), Entr("87")]),
    "9F" : Map([Entr("72"), Entr("8B")]),
    "A0" : Map([Entr("92"), Entr("11D")]),
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
    "AF" : Map([Entr("AD"), Entr("AFb", req=EntrReq.SMALL)]),
    "AFb" : Map([Entr("AF", req=EntrReq.SMALL), Entr("105")]), # right side
    "B0" : Map([Entr("AD"), Entr("B8")]),
    "B1" : Map([Entr("A8"), Entr("B5"), Entr("B7", req=EntrReq.MAGIC_SEAL_2), Entr("BD")]),
    "B2" : Map([Entr("A9"), Entr("BB")]),
    "B3" : Map([Entr("AA"), Entr("BB")]),
    "B4" : Map([Entr("AE"), Entr("BB")]),
    "B5" : Map([Entr("B1"), Entr("B9")]),
    "B6" : Map([Entr("BA")], loc_B6),
    "B7" : Map([Entr("B1"), Entr("BA")]),
    "B8" : Map([Entr("B0")], loc_B8),
    "B9" : Map([Entr("B5"), Entr("B9b", req=EntrReq.SMALL)], loc_B9),
    "B9b" : Map([Entr("B9", req=EntrReq.SMALL), Entr("BCb")]),
    "BA" : Map([Entr("B6", req=EntrReq.MAGIC_SEAL_2), Entr("B7")], loc_BA),
    "BB" : Map([Entr("B2"), Entr("B3"), Entr("B4"), Entr("BC"), Entr("BE")], loc_BB),
    "BC" : Map([Entr("BB"), Entr("BCb")]),
    "BCb" : Map([Entr("B9b", req=EntrReq.HEIGHT), Entr("BC"), Entr("DA")], loc_BCb),
    "BD" : Map([Entr("B1")]),
    "BE" : Map([Entr("BB")]),
    "BF" : Map([Entr("AA")]),
    "C0" : Map([Entr("C0b"), Entr("C3"), Entr("D9")]),
    "C0b" : Map([Entr("C0")]), # left side
    "C1" : Map([Entr("C6"), Entr("DA")]),
    "C2" : Map([Entr("C7h"), Entr("DE")], loc_C2),
    "C3" : Map([Entr("C0", req=EntrReq.HEIGHT), Entr("C7f"), Entr("C7g", req=EntrReq.HEIGHT)], loc_C3),
    "C4" : Map([Entr("C4b", req=EntrReq.HEIGHT), Entr("C7d")]),
    "C4b" : Map([Entr("C4"), Entr("C7e")], loc_C4b),
    "C5" : Map([Entr("C7b"), Entr("C7c", req=EntrReq.HEIGHT)]),
    "C6" : Map([Entr("C1"), Entr("C7")], loc_C6),

    # tower
    "C7" : Map([Entr("C6"), Entr("CB")]),
    "C7b" : Map([Entr("C5"), Entr("CB")]), # 2nd floor
    "C7c" : Map([Entr("C5"), Entr("CA")]), # 3rd floor
    "C7d" : Map([Entr("C4"), Entr("CA")]), # 4th floor
    "C7e" : Map([Entr("C4b"), Entr("C9")]),
    "C7f" : Map([Entr("C9"), Entr("C3")]),
    "C7g" : Map([Entr("C3"), Entr("C8")]),
    "C7h" : Map([Entr("C2"), Entr("C8b")], loc_C7h),

    "C8" : Map([Entr("C7g"), Entr("C8b", req=EntrReq.HEIGHT)]),
    "C8b" : Map([Entr("C7h", req=EntrReq.MAGIC_SEAL_3), Entr("C8"), Entr("DC")]),
    "C9" : Map([Entr("C7e"), Entr("C7f", req=EntrReq.HEIGHT)]),
    "CA" : Map([Entr("C7c"), Entr("C7d", req=EntrReq.HEIGHT)]),
    "CB" : Map([Entr("C7"), Entr("C7b", req=EntrReq.HEIGHT), Entr("CC")], loc_CB),
    "CC" : Map([Entr("CB"), Entr("D8")]),
    "CD" : Map([Entr("CF")]),
    "CE" : Map([Entr("D2"), Entr("DF")]),
    "CF" : Map([Entr("CD"), Entr("D3")]),
    "D0" : Map([Entr("E0", req=EntrReq.HEIGHT), Entr("E1")]),
    "D1" : Map([Entr("E2", req=EntrReq.HEIGHT), Entr("E3")]),
    "D2" : Map([Entr("CE"), Entr("D2b"), Entr("E4", req=EntrReq.HEIGHT)]),
    "D2b" : Map([Entr("D2", req=EntrReq.HEIGHT), Entr("E5")]), # lower area
    "D3" : Map([Entr("CF"), Entr("D4")]),
    "D4" : Map([Entr("D3"), Entr("D4b"), Entr("D8")]),
    "D4b" : Map([Entr("D4", req=EntrReq.DISTANCE), Entr("E0")]), # lower area
    "D5" : Map([Entr("E1", req=EntrReq.HEIGHT), Entr("E2")]),
    "D6" : Map([Entr("E3", req=EntrReq.HEIGHT), Entr("E4")]),
    "D7" : Map([Entr("DD"), Entr("E5", req=EntrReq.MEDIUM_HEIGHT), Entr("E6")]),
    "D8" : Map([Entr("CC", req=EntrReq.MEDIUM_HEIGHT), Entr("D4")]),
    "D9" : Map([Entr("C0b"), Entr("139")]),
    "DA" : Map([Entr("BCb"), Entr("C1")]),
    "DB" : Map([Entr("E6"), Entr("E7")], loc_DB),
    "DC" : Map([Entr("C8")]),
    "DD" : Map([Entr("D7")]),
    "DE" : Map([Entr("C2")]),
    "DF" : Map([Entr("CE")]),
    "E0" : Map([Entr("D0"), Entr("D4")]),
    "E1" : Map([Entr("D0"), Entr("D5")]),
    "E2" : Map([Entr("D1", req=EntrReq.HEIGHT), Entr("D5", req=EntrReq.HEIGHT)]),
    "E3" : Map([Entr("D1"), Entr("D6")]),
    "E4" : Map([Entr("D2"), Entr("D6")]),
    "E5" : Map([Entr("D2"), Entr("D7")]),
    "E6" : Map([Entr("D7"), Entr("DB", req=EntrReq.MAGIC_SEAL_5)]),
    "E7" : Map([Entr("DB"), Entr("15E")]),
    "E8" : Map([Entr("E8b"), Entr("EB")]),
    "E8b" : Map([Entr("E8"), Entr("101")]),
    "E9" : Map([Entr("EC"), Entr("102")]),
    "EA" : Map([Entr("ECb")], loc_EA),
    "EB" : Map([Entr("E8"), Entr("ECd")]),
    "EC"  : Map([Entr("E9", req=EntrReq.BIGGER_HEIGHT), Entr("EA", req=EntrReq.HEIGHT_AND_DISTANCE), Entr("ECb", req=EntrReq.HEIGHT), Entr("ED")]), # upper entrance
    "ECb" : Map([Entr("ECc")], loc_ECb), # middle area
    "ECc" : Map([Entr("ECb", req=EntrReq.HEIGHT), Entr("ED")], loc_ECc), # lower entrance
    "ECd" : Map([Entr("EB"), Entr("ECc", req=EntrReq.HEIGHT), Entr("EE")]), # bottom area
    "ED" : Map([Entr("ECc"), Entr("EC"), Entr("EF", req=EntrReq.HEIGHT), Entr("106")]),
    "EE" : Map([Entr("ECd"), Entr("103", req=EntrReq.DISTANCE)]),
    "EF" : Map([Entr("ED"), Entr("F1")]),
    "F0" : Map([Entr("F8b")]), # todo: rock prize game
    "F1" : Map([Entr("EF"), Entr("F2", req=EntrReq.DISTANCE)], loc_F1),
    "F2" : Map([Entr("F1"), Entr("F3"), Entr("108")]),
    "F3" : Map([Entr("F2"), Entr("F4"), Entr("F7")]),
    "F4" : Map([Entr("F3"), Entr("F5")]),
    "F5" : Map([Entr("F4"), Entr("F6", req=EntrReq.HEIGHT), Entr("109")], loc_F5),
    "F6" : Map([Entr("F5"), Entr("A1")]),
    "F7" : Map([Entr("F3", req=EntrReq.RAHAB_OR_HEIGHT), Entr("F8b", req=EntrReq.HEIGHT)]),
    "F8" : Map([Entr("F8b", req=EntrReq.HEIGHT), Entr("F9"), Entr("FA")]),
    "F8b" : Map([Entr("F0"), Entr("F7"), Entr("F8")]), # upper area
    "F9" : Map([Entr("F8", req=EntrReq.HEIGHT), Entr("F9b")]),
    "F9b" : Map([Entr("F9"), Entr("104")]), # left area
    "FA" : Map([Entr("F8"), Entr("FD")]),
    "FB" : Map([Entr("FC"), Entr("105"), Entr("107")]),
    "FC" : Map([Entr("FB"), Entr("FE", req=EntrReq.MAGIC_SEAL_3)]),
    "FD" : Map([Entr("FA", req=EntrReq.RAHAB), Entr("FF", req=EntrReq.RAHAB_AND_HEIGHT)]),
    "FE" : Map([Entr("FC"), Entr("100")], loc_FE),
    "FF" : Map([Entr("FD", req=EntrReq.RAHAB), Entr("100", req=EntrReq.RAHAB)], loc_FF),
    "100" : Map([Entr("FE", req=EntrReq.RAHAB), Entr("FF", req=EntrReq.RAHAB)]),
    "101" : Map([Entr("7B"), Entr("E8b")]),
    "102" : Map([Entr("6Db"), Entr("E9")]),
    "103" : Map([Entr("EE"), Entr("10A")]),
    "104" : Map([Entr("F9b"), Entr("112")]),
    "105" : Map([Entr("AFb"), Entr("FB")]),
    "106" : Map([Entr("ED")]),
    "107" : Map([Entr("FB")]),
    "108" : Map([Entr("F2")]),
    "109" : Map([Entr("F5")]),
    "10A" : Map([Entr("103"), Entr("10Ab", req=EntrReq.ZEPHYR)]),
    "10Ab" : Map([Entr("10A"), Entr("10B")]),
    "10B" : Map([Entr("10Ab"), Entr("10C")]),
    "10C" : Map([Entr("10B", req=EntrReq.HEIGHT), Entr("10D", req=EntrReq.HEIGHT), Entr("10E"), Entr("116")]),
    "10D" : Map([Entr("10C"), Entr("111")]),
    "10E" : Map([Entr("10C"), Entr("111")]),
    "10F" : Map([Entr("110b")], loc_10F),
    "110" : Map([Entr("110b", req=EntrReq.HEIGHT), Entr("111")]),
    "110b" : Map([Entr("10F"), Entr("110"), Entr("112")]),
    "111" : Map([Entr("10D", req=EntrReq.HEIGHT), Entr("10E"), Entr("110", req=EntrReq.HEIGHT), Entr("113"), Entr("114")]),
    "112" : Map([Entr("104"), Entr("110b")]),
    "113" : Map([Entr("111"), Entr("115")]),
    "114" : Map([Entr("111"), Entr("11A")]),
    "115" : Map([Entr("113"), Entr("117"), Entr("119")]),
    "116" : Map([Entr("10C")], loc_116),
    "117" : Map([Entr("115"), Entr("118", req=EntrReq.MAGIC_SEAL_4)]),
    "118" : Map([Entr("117")], loc_118),
    "119" : Map([Entr("115")]),
    "11A" : Map([Entr("114")]),
    "11B" : Map([Entr("11C")], loc_11B),
    "11C" : Map([Entr("11B"), Entr("11E")]),
    "11D" : Map([Entr("A0"), Entr("120")]),
    "11E" : Map([Entr("11C"), Entr("127")]),
    "11F" : Map([Entr("120"), Entr("127")]),
    "120" : Map([Entr("11D"), Entr("11F")]),
    "121" : Map([Entr("125"), Entr("159")]),
    "122" : Map([Entr("126")]),
    "123" : Map([Entr("129b"), Entr("12A")]),
    "124" : Map([Entr("12A"), Entr("124b", req=EntrReq.FLIGHT)]),
    "124b" : Map([Entr("124", req=EntrReq.FLIGHT), Entr("12B")]),
    "125" : Map([Entr("121"), Entr("12B")]),
    "126" : Map([Entr("122"), Entr("12C"), Entr("12D")]),
    "127" : Map([Entr("11E"), Entr("11F"), Entr("12E")]),
    "128" : Map([Entr("129b"), Entr("12F"), Entr("13C")]),
    "129" : Map([Entr("129b"), Entr("130"), Entr("132", req=EntrReq.HEIGHT), Entr("136")]),
    "129b" : Map([Entr("123"), Entr("128"), Entr("129")]), # left side
    "12A" : Map([Entr("123"), Entr("124")]),
    "12B" : Map([Entr("124b"), Entr("125")]),
    "12C" : Map([Entr("126"), Entr("131", req=EntrReq.HEIGHT)]),
    "12D" : Map([Entr("126"), Entr("138")]),
    "12E" : Map([Entr("127"), Entr("138")]),
    "12F" : Map([Entr("128"), Entr("132")], loc_12F),
    "130" : Map([Entr("129", req=EntrReq.HEIGHT), Entr("133")]),
    "131" : Map([Entr("12C"), Entr("134"), Entr("135")]),
    "132" : Map([Entr("129"), Entr("12F", req=EntrReq.MAGIC_SEAL_4), Entr("13B")]),
    "133" : Map([Entr("130"), Entr("136"), Entr("137")]), # todo: konami man
    "134" : Map([Entr("131"), Entr("137")], loc_134),
    "135" : Map([Entr("131")], loc_135),
    "136" : Map([Entr("129"), Entr("133")]),
    "137" : Map([Entr("133", req=EntrReq.HEIGHT), Entr("134")], loc_137),
    "138" : Map([Entr("12D"), Entr("12E"), Entr("139"), Entr("13A")]),
    "139" : Map([Entr("D9"), Entr("138")]),
    "13A" : Map([Entr("138")], loc_13A),
    "13B" : Map([Entr("132")]),
    "13C" : Map([Entr("128")]),
    "13D" : Map([Entr("13E")], loc_13D),
    "13E" : Map([Entr("13D"), Entr("140")], loc_13E),
    "13F" : Map([Entr("140")], loc_13F),
    "140" : Map([Entr("13E", req=EntrReq.MAGIC_SEAL_4), Entr("13F", req=EntrReq.BIGGER_HEIGHT), Entr("142b")]),
    "141" : Map([Entr("142")], loc_141),
    "142" : Map([Entr("141", req=EntrReq.BIG_HEIGHT), Entr("143", req=EntrReq.HEIGHT), Entr("14B", req=EntrReq.HEIGHT)]),
    "142b" : Map([Entr("140"), Entr("148", req=EntrReq.BIG_HEIGHT), Entr("149")]), # upper area
    "143" : Map([Entr("142", req=EntrReq.HEIGHT), Entr("145")]),
    "144" : Map([Entr("14D"), Entr("158")]),
    "145" : Map([Entr("143"), Entr("14D"), Entr("150")]),
    "146" : Map([Entr("147"), Entr("14D", req=EntrReq.HEIGHT), Entr("15C", req=EntrReq.HEIGHT)]),
    "147" : Map([Entr("146", req=EntrReq.HEIGHT)], loc_147),
    "148" : Map([Entr("142b")]),
    "149" : Map([Entr("142b"), Entr("14A")]),
    "14A" : Map([Entr("149", req=EntrReq.BIGGER_HEIGHT), Entr("14Ec"), Entr("15A")]),
    "14B" : Map([Entr("142"), Entr("14Bb", req=EntrReq.HEIGHT), Entr("14C")]),
    "14Bb" : Map([Entr("14B"), Entr("14E")], loc_14Bb), # upper area
    "14C" : Map([Entr("14B", req=EntrReq.BIGGER_HEIGHT), Entr("14F")]),
    "14D" : Map([Entr("144"), Entr("145", req=EntrReq.MEDIUM_HEIGHT), Entr("146"), Entr("15B")]),
    "14E" : Map([Entr("14Bb"), Entr("14Eb")], loc_14E),
    "14Eb" : Map([Entr("14E", req=EntrReq.MEDIUM_HEIGHT), Entr("156")]), # lower right area
    "14Ec" : Map([Entr("14A"), Entr("154")]), # upper area
    "14F" : Map([Entr("14C"), Entr("156")]),
    "150" : Map([Entr("145"), Entr("152"), Entr("157")]),
    "151" : Map([Entr("14D", req=EntrReq.HEIGHT), Entr("152", req=EntrReq.MEDIUM_HEIGHT)]),
    "152" : Map([Entr("150"), Entr("151")]),
    "153" : Map([Entr("154")]),
    "154" : Map([Entr("14Ec"), Entr("153", req=EntrReq.MEDIUM_HEIGHT), Entr("155")]),
    "155" : Map([Entr("154", req=EntrReq.BIGGER_HEIGHT), Entr("156b")]),
    "156" : Map([Entr("14F"), Entr("156b", req=EntrReq.HEIGHT)]),
    "156b" : Map([Entr("14Eb"), Entr("155", req=EntrReq.MEDIUM_HEIGHT), Entr("156")]), # upper area
    "157" : Map([Entr("150"), Entr("159")]),
    "158" : Map([Entr("50"), Entr("144")]),
    "159" : Map([Entr("121"), Entr("157")]),
    "15A" : Map([Entr("14A")]),
    "15B" : Map([Entr("14D")]),
    "15C" : Map([Entr("146")]),
    
    # The Abyss
    "15D" : Map([]), # Menace
    "15E" : Map([Entr("E7"), Entr("15F")]),
    "15F" : Map([Entr("15E", req=EntrReq.HEIGHT), Entr("15Fb", req=EntrReq.HEIGHT), Entr("17E")]),
    "15Fb" : Map([Entr("15F", req=EntrReq.HEIGHT), Entr("160")]),
    "160" : Map([Entr("15Fb", req=EntrReq.MEDIUM_HEIGHT), Entr("161")]),
    "161" : Map([Entr("160"), Entr("162")]),
    "162" : Map([Entr("161"), Entr("163")]),
    "163" : Map([Entr("162", req=EntrReq.HEIGHT), Entr("164")]),
    "164" : Map([Entr("163"), Entr("165", req=EntrReq.MEDIUM_HEIGHT)], loc_164),
    "165" : Map([Entr("164", req=EntrReq.MEDIUM_HEIGHT), Entr("166", req=EntrReq.MEDIUM_HEIGHT)]),
    "166" : Map([Entr("165", req=EntrReq.MEDIUM_HEIGHT), Entr("167")]),
    "167" : Map([Entr("166"), Entr("168")]),
    "168" : Map([Entr("167"), Entr("169")]),
    "169" : Map([Entr("168", req=EntrReq.MEDIUM_HEIGHT), Entr("16A")]),
    "16A" : Map([Entr("169", req=EntrReq.MEDIUM_HEIGHT), Entr("16B", req=EntrReq.HEIGHT)]),
    "16B" : Map([Entr("16A", req=EntrReq.MEDIUM_HEIGHT), Entr("16C", req=EntrReq.HEIGHT)]),
    "16C" : Map([Entr("16B", req=EntrReq.MEDIUM_HEIGHT), Entr("16D", req=EntrReq.HEIGHT)]),
    "16D" : Map([Entr("16C"), Entr("16E")]),
    "16E" : Map([Entr("16D"), Entr("16F")]),
    "16F" : Map([Entr("16E", req=EntrReq.BIGGER_HEIGHT), Entr("170", req=EntrReq.BIGGER_HEIGHT)]),
    "170" : Map([Entr("16F", req=EntrReq.BIGGER_HEIGHT), Entr("170b", req=EntrReq.BIGGER_HEIGHT)]),
    "170b" : Map([Entr("171", req=EntrReq.MAGIC_SEAL_5_AND_HEIGHT), Entr("17F")]), # upper right area
    "171" : Map([Entr("170"), Entr("172")], loc_171),
    "172" : Map([Entr("171"), Entr("173")]),
    "173" : Map([Entr("172"), Entr("174")]),
    "174" : Map([Entr("173", req=EntrReq.HEIGHT), Entr("175", req=EntrReq.MEDIUM_HEIGHT)]),
    "175" : Map([Entr("174", req=EntrReq.HEIGHT), Entr("176", req=EntrReq.MEDIUM_HEIGHT)]),
    "176" : Map([Entr("175", req=EntrReq.HEIGHT), Entr("177", req=EntrReq.MEDIUM_HEIGHT)]),
    "177" : Map([Entr("176"), Entr("178", req=EntrReq.MEDIUM_HEIGHT)]),
    "178" : Map([Entr("177"), Entr("179")]),
    "179" : Map([Entr("17A")]),
    "17A" : Map([Entr("179"), Entr("17Ab", req=EntrReq.HEIGHT)]),
    "17Ab" : Map([Entr("17A"), Entr("17B")]),
    "17B" : Map([Entr("17Ab"), Entr("17C"), Entr("181")]),
    "17C" : Map([Entr("17B"), Entr("17Cb"), Entr("180")]),
    "17Cb" : Map([Entr("17C", req=EntrReq.HEIGHT), Entr("17D")]),
    "17D" : Map([Entr("17Cb"), Entr("15D")]),
    "17E" : Map([Entr("15F")]),
    "17F" : Map([Entr("170b")]),
    "180" : Map([Entr("17C")]),
    "181" : Map([Entr("17B")]),
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

    menu_region.add_exits({"02": "Start"}, None)
