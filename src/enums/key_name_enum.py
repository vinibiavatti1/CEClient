"""
Keyboard key name enumeration.
"""
from enum import Enum


class KeyNameEnum(Enum):
    """
    Key name enum.
    """

    FIRE = 'Fire'
    USE_ITEM = 'UseItem'
    CHANGE_ITEM = 'ChangeItem'
    DROP_ITEM = 'DropItem'
    JUMP = 'Jump'
    PITCH_PLUS = 'Pitch+'
    PITCH_MINUS = 'Pitch-'
    ROLL_PLUS = 'Roll+'
    ROLL_MINUS = 'Roll-'
    FORWARD_PLUS = 'Forward+'
    FORWARD_MINUS = 'Forward-'
    YAW_PLUS = 'Yaw+'
    YAW_MINUS = 'Yaw-'

    @classmethod
    def has_value(cls, value: str) -> bool:
        """
        Validates if enum contains value.
        """
        return value in cls._value2member_map_
