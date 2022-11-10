"""
Data service to manipulate ROM app data.
"""
from models.data_model import DataModel
import os
import json
from app_constants import AppConstants
from services.path_service import PathService
from typing import Any
from services.dialog_service import DialogService


class DataService:
    """
    Data service.
    """

    data: DataModel = DataModel()

    @classmethod
    def load_data(cls) -> None:
        """
        Load data from file.
        """
        if not os.path.exists(PathService.get_data_json_path()):
            cls.data = cls.create_data_file()
            return
        with open(PathService.get_data_json_path(), 'r') as file:
            json_str = file.read()
        json_object = json.loads(json_str)
        cls.validate_json_data_version_and_load(json_object)

    @classmethod
    def validate_json_data_version_and_load(cls, json_object: Any) -> None:
        """
        Check data.json version.
        """
        data_version = None
        if 'version' in json_object:
            data_version = json_object['version']
        if AppConstants.DATA_VERSION != data_version:
            ok = DialogService.question(
                None,
                f'The version of the data.json file is different of the ' +
                f'application version (Data version: {data_version}, ' +
                f'App data version: ' +
                f'{AppConstants.DATA_VERSION}). The current data.json file ' +
                f'is incompatible. Do you want to replace the ' +
                f'data.json file with the new version?'
            )
            if not ok:
                raise Exception(
                    'The application will be closed due to the incompatible ' +
                    'data.json file version.'
                )
            cls.data = cls.create_data_file()
        else:
            cls.data = DataModel.from_json(json_object)

    @classmethod
    def create_data_file(cls) -> DataModel:
        """
        Create initial datafile.
        """
        data_model = DataModel()
        with open(PathService.get_data_json_path(), 'w+') as file:
            file.write(data_model.to_json())
        return data_model

    @classmethod
    def get_data(cls) -> DataModel:
        """
        Get app data.
        """
        return cls.data

    @classmethod
    def save_data(cls, data: DataModel) -> None:
        """
        Save app date.
        """
        cls.data = data
        with open(PathService.get_data_json_path(), 'w+') as file:
            file.write(data.to_json())
