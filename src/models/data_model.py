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
                'server_name': 'EU Server',
                'server_ip': '89.38.98.12:24711'
            },
            {
                'server_name': 'US Server',
                'server_ip': '67.199.173.146:24711'
            }
        ]
        self.last_server_ip: Optional[str] = '89.38.98.12:24711'
        self.last_server_name: str = 'EU Server'
        self.ce_execution_command: str = 'ce.exe'
        self.additional_arguments: str = ''
        self.version: int = 1

    @classmethod
    def from_json(cls, json_object: dict[str, Any]) -> 'DataModel':
        """
        Create DataModel from json.
        """
        data_model = cls()
        data_model.nickname = json_object['nickname']
        data_model.server_list = json_object['server_list']
        data_model.last_server_name = json_object['last_server_name']
        data_model.last_server_ip = json_object['last_server_ip']
        data_model.fov = json_object['fov']
        data_model.mousesens = json_object['mousesens']
        data_model.viewdist = json_object['viewdist']
        data_model.latency = json_object['latency']
        data_model.ce_execution_command = json_object['ce_execution_command']
        data_model.additional_arguments = json_object['additional_arguments']
        data_model.version = json_object['version']
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
