"""
Auto execute shortcut module.
"""
from services.data_service import DataService
from services.process_service import ProcessService
from app_constants import AppConstants
import argparse


class AutoConnect:
    """
    Auto execute connection class.
    """

    @classmethod
    def execute(cls, args: argparse.Namespace) -> None:
        """
        Auto execute application.
        """
        data = DataService.get_data()
        nickname = data.nickname

        # If -ip argument provided
        if args.ip:
            server_ip = args.ip

        # If -sn (--server-name) argument provided
        elif args.server_name:
            server_ip = None
            for server in data.server_list:
                if server['server_name'] == args.server_name:
                    server_ip = server['server_ip']
                    break
            if server_ip is None:
                raise Exception(
                    f'Could not find server name "{args.server_name}" in ' +
                    'server list.'
                )

        # If no argument provided, get last IP from data.json
        else:
            server_ip = data.last_server_ip
            if server_ip is None:
                if len(data.server_list) == 0:
                    raise Exception(
                        'No server found to connect. Please, open the ' +
                        'application and register at least one server, ' +
                        'or use the "-ip" argument to provide a static IP ' +
                        'address.'
                    )
                server_ip = data.server_list[0]['server_ip']

        # Execute connection
        ProcessService.execute(server_ip, nickname)
