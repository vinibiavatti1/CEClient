"""
Advanced Config frame module.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from typing import TYPE_CHECKING
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
)
from app_constants import AppConstants
from enums.frame_enum import FrameEnum
from frames.connection_frame import ConnectionFrame
from services.data_service import DataService
from services.dialog_service import DialogService

from services.game_config_service import GameConfigService
from services.setup_service import SetupService
if TYPE_CHECKING:
    from main_window import MainWindow


class AdvancedConfigFrame(QFrame):
    """
    Advanced Config frame class.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new ConfigFrame.
        """
        super().__init__(main_window)
        self.__main_window = main_window
        self.__build()
        self.__register_handlers()

    ###########################################################################
    # Handlers
    ###########################################################################

    def __register_handlers(self) -> None:
        """
        Register frame event handlers.
        """
        self.__save_button.clicked.connect(
            self.__handle_save
        )
        self.__reinstall_button.clicked.connect(
            self.__handle_reinstall
        )

    def __handle_save(self) -> None:
        """
        Handle save button click.
        """
        data = DataService.get_data()
        data.ce_execution_command = self.__ce_exec_command.currentText()
        data.additional_arguments = self.__additional_arguments.text()
        DataService.save_data(data)
        self.__main_window.set_central_widget(
            FrameEnum.CONNECTION_FRAME
        )

    def __handle_reinstall(self) -> None:
        """
        Handle reinstall game event.
        """
        ok = DialogService.question(
            self,
            'The game will be reinstalled. All in-game configurations, ' +
            'save points and map folders will be deleted. Proceed?'
        )
        if not ok:
            return
        DialogService.progress(
            self,
            f'Reinstalling game... ({AppConstants.GAME_NAME})',
            SetupService.reinstall_game
        )
        DialogService.info(
            self,
            'Game reinstalled successfully!'
        )

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __build(self) -> None:
        """
        Build frame.
        """
        # Data
        data = DataService.get_data()

        # Grid
        self.__grid = QVBoxLayout()
        self.__grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__grid)

        # CE exec file
        self.__grid.addWidget(QLabel(
            'CE Execution Command: (Default: ce.exe)', self
        ))
        self.__ce_exec_command = QComboBox(self)
        self.__ce_exec_command.setEditable(True)
        self.__ce_exec_command.addItem('ce.exe')
        self.__ce_exec_command.addItem('game.exe')
        self.__ce_exec_command.addItem('wine ce.exe')
        self.__ce_exec_command.addItem('wine game.exe')
        self.__ce_exec_command.setCurrentText(data.ce_execution_command)
        self.__ce_exec_command.setPlaceholderText(
            'Enter the execution command'
        )
        self.__grid.addWidget(self.__ce_exec_command)

        # Additional Arguments
        self.__grid.addWidget(QLabel(
            'Additional Execution Arguments:', self
        ))
        self.__additional_arguments = QLineEdit(self)
        self.__additional_arguments.setText(data.additional_arguments)
        self.__additional_arguments.setPlaceholderText(
            'Enter the additional arguments to put after CE execution command'
        )
        self.__grid.addWidget(self.__additional_arguments)

        # Save button
        self.__save_button = QPushButton('Save', self)
        self.__save_button.setIcon(QIcon(':save-icon'))
        self.__grid.addWidget(self.__save_button)

        # Reinstall game button
        self.__grid.addWidget(QLabel(
            f'If you want to reinstall the game, click on the button below.'
        ))
        self.__reinstall_button = QPushButton('Reinstall Game', self)
        self.__reinstall_button.setIcon(QIcon(':reinstall'))
        self.__grid.addWidget(self.__reinstall_button)
