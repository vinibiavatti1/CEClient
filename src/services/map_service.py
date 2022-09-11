"""
Map service module.
"""
import os
from services.path_service import PathService
from models.map_model import MapModel


class MapService:
    """
    Service with logic for map manager.

    Levels.nfo example:
    Name:No mans land Val:128
    Name:Breakpoint Val:129
    Name:The palace Val:130
    Name:Carrier war Val:131
    Name:The airbase Val:132
    Name:Fortress Val:133
    Name:Fever valley Val:134
    """
    NATIVE_MAPS: list[int] = [128, 129, 130, 131, 132, 133, 134]
    MAP_RECORDS_FILE: str = 'levels.nfo'
    MAP_RECORD_NAME_KEY: str = 'Name:'
    MAP_RECORD_VALUE_KEY: str = 'Val:'

    @classmethod
    def list_maps(cls) -> list[MapModel]:
        """
        List the maps from an instance checking the levels.nfo file.
        """
        levels_nfo = os.path.join(
            PathService.get_game_path(),
            cls.MAP_RECORDS_FILE
        )
        with open(levels_nfo, 'r') as file:
            maps_str = file.readlines()
        return cls.map_levels_nfo_to_map_models(maps_str)

    @classmethod
    def map_levels_nfo_to_map_models(cls, levels_nfo_content: list[str]
                                     ) -> list[MapModel]:
        """
        Convert str levels.nfo file format to map model list.
        """
        map_list: list[MapModel] = []
        for line in levels_nfo_content:
            stripped_line = line.strip()
            if len(stripped_line) == 0:
                continue
            if cls.MAP_RECORD_VALUE_KEY not in stripped_line:
                continue
            map_record_str = stripped_line.split(cls.MAP_RECORD_VALUE_KEY)
            if len(map_record_str) != 2:
                continue
            map_name = map_record_str[0].replace(
                cls.MAP_RECORD_NAME_KEY, ''
            ).strip()
            map_val = map_record_str[1].strip()
            try:
                map_val_int = int(map_val)
            except ValueError as err:
                print(err)
                continue
            map_list.append(MapModel(map_name, map_val_int))
        return map_list

    @classmethod
    def is_native_map(cls, map: MapModel) -> bool:
        """
        Return True if the map is native.
        """
        return map.val in cls.NATIVE_MAPS

    @classmethod
    def update_levels_nfo_file(cls, maps: list[MapModel]) -> None:
        """
        Update the levels.nfo file by a list of MapModel.
        """
        if len(maps) == 0:
            return
        levels_nfo = os.path.join(
            PathService.get_game_path(),
            cls.MAP_RECORDS_FILE
        )
        content = cls.generate_levels_nfo_content(maps)
        with open(levels_nfo, 'w') as file:
            file.write(content)

    @classmethod
    def generate_levels_nfo_content(cls, maps: list[MapModel]) -> str:
        """
        Generate LEVELS.nfo file format content.
        """
        content = ''
        for map in maps:
            content += f'{cls.MAP_RECORD_NAME_KEY}{map.name} '
            content += f'{cls.MAP_RECORD_VALUE_KEY}{map.val}'
            content += '\n'
        return content
