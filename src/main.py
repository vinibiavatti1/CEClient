"""
App entry-point module.
"""
import sys
from app_info import AppInfo
from auto_connect import AutoConnect
from services.data_service import DataService
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from services.dialog_service import DialogService
from services.setup_service import SetupService


AUTO_EXEC_ARGUMENT = '--auto-connect'


def main(argv: list[str]) -> None:
    """
    App main method.
    """
    app = QApplication(argv)
    if not SetupService.is_game_installed():
        DialogService.progress(
            None,
            f'Installing Game... ({AppInfo.GAME_NAME})',
            SetupService.install_game
        )
    DataService.load_data()
    main_window = MainWindow()
    if AUTO_EXEC_ARGUMENT in argv:
        AutoConnect.execute()
        sys.exit(0)
    main_window.show()
    sys.exit(app.exec_())


# Initialization
if __name__ == '__main__':
    main(sys.argv)
