"""
Data service to manipulate ROM app data.
"""
from models.data_model import DataModel
import os
import json

from services.path_service import PathService


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
