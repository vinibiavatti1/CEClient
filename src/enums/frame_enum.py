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
