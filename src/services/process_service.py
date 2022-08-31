"""
Process service to work with ce.exe process and lobby.exe.
"""
import psutil
import os

from services.path_service import PathService


class ProcessService:
    """
    Process service.
    """

    CE_PROCESS_NAME: str = 'ce.exe'
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
    def execute(cls, server_ip: str, nickname: str) -> None:
        """
        Execute game connection to the server.
        """
        ce_command = f'ce.exe +connect {server_ip} +name "{nickname}"'
        command_line = f'cd "{PathService.get_game_path()}" && {ce_command}'
        cls.kill_ce_processes()
        print(f'Executing command: {command_line}')
        os.system(command_line)
        cls.kill_ce_processes()
