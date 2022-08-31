"""
Path utilities.
"""
import sys
import os


class PathService:
    """
    Path service class.
    """

    @classmethod
    def get_game_path(cls) -> str:
        """
        Return game folder path.
        """
        return os.path.join(cls.get_current_dir(), 'game')

    @classmethod
    def get_zip_path(cls) -> str:
        """
        Return game zip folder path.
        """
        return os.path.join(cls.get_data_path(), 'game.zip')

    @classmethod
    def get_data_path(cls) -> str:
        """
        Return game folder path.
        """
        return os.path.join(cls.get_current_dir(), 'data', 'data.json')

    @classmethod
    def get_default_cfg_path(cls) -> str:
        """
        Return game folder path.
        """
        return os.path.join(cls.get_game_path(), 'default.cfg')

    @classmethod
    def get_current_dir(cls) -> str:
        """
        Get current dir depending the way the app is running: .exe or .py.
        """
        if getattr(sys, 'frozen', False):
            return os.getcwd()
        elif __file__:
            return os.path.dirname(sys.argv[0])
        else:
            raise Exception('Cannot get root directory')
