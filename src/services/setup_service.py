"""
Setup utilities module.
"""
import shutil
import zipfile
import os
from services.path_service import PathService


class SetupService:
    """
    Setup utilities.
    """

    ZIP_FOLDER_NAME: str = 'game.zip'
    CE_EXEC_FILE_NAME: str = 'ce.exe'

    @classmethod
    def install_game(cls) -> None:
        """
        Unzip the game zip folder.
        """
        zip_path = PathService.get_zip_path()
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(
                PathService.get_game_path()
            )

    @classmethod
    def is_game_installed(cls) -> bool:
        """
        Check if the game zip folder was extracted.
        """
        return os.path.exists(os.path.join(
            PathService.get_game_path(), cls.CE_EXEC_FILE_NAME
        ))

    @classmethod
    def reinstall_game(cls) -> None:
        """
        Delete the game folder.
        """
        path = PathService.get_game_path()
        if os.path.exists(path):
            shutil.rmtree(path)
        cls.install_game()
