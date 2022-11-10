"""
Argument parser class.
"""
import argparse
from app_constants import AppConstants


class ArgsParserService:
    """
    Argument parser service class.
    """

    def __init__(self) -> None:
        """
        Create arg parse class.
        """
        self.__build_parser()

    def parse(self) -> argparse.Namespace:
        """
        Parse app arguments and return a namespace.
        """
        return self.parser.parse_args()

    def __build_parser(self) -> None:
        """
        Build argument parser.
        """
        self.parser = argparse.ArgumentParser(prog=AppConstants.APP_TITLE)
        self.parser.add_argument(
            '-ac',
            '--auto-connect',
            action='store_true',
            help='Auto connect to server'
        )
        self.parser.add_argument(
            '-ip',
            '--ip',
            help='Specify IP address to auto connect'
        )
        self.parser.add_argument(
            '-sn',
            '--server-name',
            help='Specify server name from server list to auto connect'
        )
