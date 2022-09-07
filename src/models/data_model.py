"""
Data model.
"""
import json
from typing import Any, Optional


class DataModel:
    """
    Data model class.
    """

    def __init__(self) -> None:
        """
        Create a new DataModel.
        """
        self.nickname = 'CEPlayer'
        self.fov = 200
        self.mousesens = 9
        self.viewdist = 3000
        self.latency = 0
        self.server_list: list[dict[str, str]] = [
            {
                'server_name': 'codenameeaglemultiplayer.com',
                'server_ip': '89.38.98.12:24711'
            },
            {
                'server_name': 'US Server',
                'server_ip': '67.199.173.146:24711'
            }
        ]
        self.last_server_ip: Optional[str] = '89.38.98.12:24711'
        self.last_server_index: int = 0

    @classmethod
    def from_json(cls, json_object: dict[str, Any]) -> 'DataModel':
        """
        Create DataModel from json.
        """
        data_model = cls()
        data_model.nickname = json_object['nickname']
        data_model.server_list = json_object['server_list']
        data_model.last_server_index = json_object['last_server_index']
        data_model.last_server_ip = json_object['last_server_ip']
        data_model.fov = json_object['fov']
        data_model.mousesens = json_object['mousesens']
        data_model.viewdist = json_object['viewdist']
        data_model.latency = json_object['latency']
        return data_model

    ###########################################################################
    # Public Methods
    ###########################################################################

    def to_json(self) -> str:
        """
        Convert class to JSON.
        """
        dct = dict(self.__dict__)
        return json.dumps(dct, indent=4)
