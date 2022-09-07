"""
Auto execute shortcut module.
"""


from services.data_service import DataService
from services.process_service import ProcessService


class AutoExec:
    """
    Auto execute connection class.
    """

    @classmethod
    def execute(cls) -> None:
        """
        Auto execute application.
        """
        data = DataService.get_data()
        server_ip = data.last_server_ip
        if server_ip is None:
            if len(data.server_list) == 0:
                raise Exception(
                    'No server found to connect. Please, open the ' +
                    'application and register at least one server.'
                )
            server_ip = data.server_list[0]['server_ip']
        nickname = data.nickname
        ProcessService.execute(server_ip, nickname)
