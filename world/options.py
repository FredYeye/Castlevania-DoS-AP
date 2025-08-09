from worlds.AutoWorld import PerGameCommonOptions
from dataclasses import dataclass
from Options import DefaultOnToggle

class TestOption(DefaultOnToggle):
    """test option"""
    display_name = "test option"

@dataclass
class cvdosOptions(PerGameCommonOptions):
    test_option: TestOption
