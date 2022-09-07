"""
App entry-point module.
"""
import sys
from auto_exec import AutoExec
from services.data_service import DataService
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from services.dialog_service import DialogService
from services.setup_service import SetupService


AUTO_EXEC_ARGUMENT = '-autoexec'


def main(argv: list[str]) -> None:
    """
    App main method.
    """
    app = QApplication(argv)
    if not SetupService.is_game_installed():
        DialogService.progress(
            None,
            'Installing Game... (Codename Eagle Multiplayer Demo)',
            SetupService.unzip_game_zip_folder
        )
    DataService.load_data()
    main_window = MainWindow()
    if AUTO_EXEC_ARGUMENT in argv:
        AutoExec.execute()
        sys.exit(0)
    main_window.show()
    sys.exit(app.exec_())


# Initialization
if __name__ == '__main__':
    main(sys.argv)
