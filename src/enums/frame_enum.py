"""
Frame enum module.
"""
from enum import Enum


class FrameEnum(Enum):
    """
    Frame enum class.
    """

    CONNECTION_FRAME = 1
    CONFIG_FRAME = 2
    SERVER_LIST_FRAME = 3
    ABOUT_FRAME = 4
    PING_TEST_FRAME = 5
    ADVANCED_CONFIG_FRAME = 6
    MAP_FRAME = 7
