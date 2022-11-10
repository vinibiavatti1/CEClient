"""
App entry-point module.
"""
import sys
from app_constants import AppConstants
from auto_connect import AutoConnect
from services.data_service import DataService
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from services.dialog_service import DialogService
from services.setup_service import SetupService
from services.args_parse_service import ArgsParserService


def main(argv: list[str]) -> None:
    """
    App main method.
    """
    app = QApplication(argv)

    # Install game
    if not SetupService.is_game_installed():
        DialogService.progress(
            None,
            f'Installing Game... ({AppConstants.GAME_NAME})',
            SetupService.install_game
        )

    # Load data file and main window
    try:
        DataService.load_data()
    except Exception as err:
        DialogService.error(None, str(err))
        sys.exit(1)

    # Create main window
    main_window = MainWindow()

    # Check for arguments
    args = ArgsParserService().parse()
    if args.auto_connect:
        try:
            AutoConnect.execute(args)
        except Exception as err:
            DialogService.error(None, str(err))
            sys.exit(1)
    else:
        main_window.show()
        sys.exit(app.exec_())


# Initialization
if __name__ == '__main__':
    main(sys.argv)
