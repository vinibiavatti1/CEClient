"""
Map model module.
"""


class MapModel:
    """
    Object to represent a map.
    """

    def __init__(self, name: str, val: int) -> None:
        """
        Create new MapModel.
        """
        self.name = name
        self.val = val

    def __str__(self) -> str:
        """
        Convert to str.
        """
        return f'LEVEL {self.val}: {self.name}'
