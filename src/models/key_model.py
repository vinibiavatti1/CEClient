"""
Key model module.
"""
from typing import Optional
from enums.key_enum import KeyEnum
from enums.key_name_enum import KeyNameEnum


class KeyModel:
    """
    Key model.
    """

    def __init__(self, key1: KeyEnum, key2: KeyEnum) -> None:
        """
        Create a new KeyModel.
        """
        self.key1 = key1
        self.key2 = key2
