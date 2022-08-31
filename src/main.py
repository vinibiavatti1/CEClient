"""
App entry-point module.
"""
import sys
from auto_exec import AutoExec
from services.data_service import DataService
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication

from services.setup_service import SetupService


def main(argv: list[str]) -> None:
    """
    App main method.
    """
    if not SetupService.is_game_installed():
        print('Installing the game...')
        SetupService.unzip_game_zip_folder()
        print('Installation done!')
    DataService.load_data()
    if '--autoexec' in argv:
        AutoExec.execute()
        sys.exit(0)
    app = QApplication(argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


# Initialization
if __name__ == '__main__':
    main(sys.argv)
