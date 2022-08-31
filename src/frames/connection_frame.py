"""
Connection frame module.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from services.data_service import DataService
from typing import TYPE_CHECKING
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox,
)
from services.game_config_service import GameConfigService

from services.process_service import ProcessService
if TYPE_CHECKING:
    from main_window import MainWindow


class ConnectionFrame(QFrame):
    """
    Connection frame class.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new ConnectionFrame.
        """
        super().__init__(main_window)
        self.__build()
        self.__register_handlers()

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

        # Nickname field
        self.__grid.addWidget(QLabel('Nickname (max 10):'))
        self.__nickname_field = QLineEdit(self)
        self.__nickname_field.setMaxLength(10)
        self.__nickname_field.setPlaceholderText('Enter the player name')
        self.__nickname_field.setText(data.nickname)
        self.__grid.addWidget(self.__nickname_field)

        # Server List
        self.__grid.addWidget(QLabel('Server List:'))
        self.__server_list = QComboBox(self)
        for server in data.server_list:
            self.__server_list.addItem(
                server['server_name'], server['server_ip']
            )
        self.__grid.addWidget(self.__server_list)
        self.__server_list.setCurrentIndex(data.last_server_index)

        # Run button
        self.__run_button = QPushButton('Connect!', self)
        self.__run_button.setIcon(QIcon(':run-icon'))
        self.__grid.addWidget(self.__run_button)

    ###########################################################################
    # Registrations
    ###########################################################################

    def __register_handlers(self) -> None:
        """
        Register frame handlers.
        """
        self.__nickname_field.textChanged.connect(
            self.__handle_nickname_change
        )
        self.__run_button.clicked.connect(
            self.__handle_connect_to_server
        )

    ###########################################################################
    # Handlers
    ###########################################################################

    def __handle_nickname_change(self, value: str) -> None:
        """
        Handle nickname field change event.
        """
        self.__run_button.setDisabled(False)
        if len(value) == 0:
            self.__run_button.setDisabled(True)

    def __handle_connect_to_server(self) -> None:
        """
        Handle connect to server button click event.
        """
        nickname = self.__nickname_field.text()
        server_ip = self.__server_list.itemData(
            self.__server_list.currentIndex()
        )
        data = DataService.get_data()
        data.last_server_ip = server_ip
        data.last_server_index = self.__server_list.currentIndex()
        DataService.save_data(data)
        ProcessService.execute(server_ip, nickname)