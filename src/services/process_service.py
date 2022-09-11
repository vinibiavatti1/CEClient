"""
Process service to work with ce.exe process and lobby.exe.
"""
import psutil
import os
from services.data_service import DataService
from services.dialog_service import DialogService

from services.path_service import PathService


class ProcessService:
    """
    Process service.
    """

    CE_PROCESS_NAME: str = 'ce.exe'
    CE_PORT: str = '24711'
    LOBBY_PROCESS_NAME: str = 'lobby.exe'

    @classmethod
    def kill_ce_processes(cls) -> None:
        """
        Kill the ce.exe and lobby.exe processes.
        """
        for p in psutil.process_iter():
            if p.name().lower() == cls.CE_PROCESS_NAME:
                p.kill()
            if p.name().lower() == cls.LOBBY_PROCESS_NAME:
                p.kill()
        print('Process ce.exe and lobby.exe killed!')

    @classmethod
    def execute(cls, server_ip: str, nickname: str) -> tuple[str, int]:
        """
        Execute game connection to the server.
        """
        data = DataService.get_data()
        exec_command = data.ce_execution_command
        additional_args = data.additional_arguments
        ce_command = f'{exec_command} +connect {server_ip} +name "{nickname}"' + \
                     f' {additional_args}'
        command_line = f'cd "{PathService.get_game_path()}" && {ce_command}'
        cls.kill_ce_processes()
        print(f'Executing command: {command_line}')
        status = os.system(command_line)
        cls.kill_ce_processes()
        return command_line, status
