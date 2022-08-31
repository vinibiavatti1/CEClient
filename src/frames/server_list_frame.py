"""
Server List frame module.
"""
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QIcon
from typing import TYPE_CHECKING
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QSpinBox,
    QLineEdit,
    QHBoxLayout,
    QListWidget,
)
from enums.frame_enum import FrameEnum
from frames.connection_frame import ConnectionFrame
from services.data_service import DataService
from services.dialog_service import DialogService

from services.game_config_service import GameConfigService
if TYPE_CHECKING:
    from main_window import MainWindow


class ServerListFrame(QFrame):
    """
    Server List frame class.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new ServerListFrame.
        """
        super().__init__(main_window)
        self.__main_window = main_window
        self.__build()
        self.__refresh_server_list()
        self.__register_handlers()

    ###########################################################################
    # Handlers
    ###########################################################################

    def __register_handlers(self) -> None:
        """
        Register frame event handlers.
        """
        self.__add_button.clicked.connect(
            self.__handle_add
        )
        self.__delete_button.clicked.connect(
            self.__handle_delete
        )

    def __handle_add(self) -> None:
        """
        Handle add button click event.
        """
        server_name = self.__server_name_field.text().strip()
        if len(server_name) == 0:
            DialogService.error(self, 'Invalid server name.')
            return
        server_ip = self.__server_ip_field.text().strip()
        if len(server_ip) == 0:
            DialogService.error(self, 'Invalid server address.')
            return
        data = DataService.get_data()
        data.server_list.append(
            dict(server_name=server_name, server_ip=server_ip)
        )
        DataService.save_data(data)
        DialogService.info(self, 'Server added successfully.')
        self.__server_name_field.setText('')
        self.__server_ip_field.setText('')
        self.__server_name_field.setFocus()
        self.__refresh_server_list()

    def __handle_delete(self) -> None:
        """
        Handle delete button click event.
        """
        current = self.__server_list.currentItem()
        if current is None:
            return
        selected = current.text()
        ok = DialogService.question(
            self,
            f'The server "{selected}" will be deleted. Proceed?'
        )
        if not ok:
            return
        current_index = self.__server_list.currentIndex()
        data = DataService.get_data()
        data.server_list.pop(current_index.row())
        DataService.save_data(data)
        self.__refresh_server_list()

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __refresh_server_list(self) -> None:
        """
        Refresh server list.
        """
        self.__server_list.clear()
        data = DataService.get_data()
        for server in data.server_list:
            self.__server_list.addItem(
                f'{server["server_name"]}: {server["server_ip"]}'
            )
        self.__delete_button.setDisabled(True)
        if len(data.server_list) > 1:
            self.__delete_button.setDisabled(False)

    def __build(self) -> None:
        """
        Build frame.
        """
        # Grid
        self.__grid = QVBoxLayout()
        self.__grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__grid)

        # Server name
        self.__grid.addWidget(QLabel('Server Name:', self))
        self.__server_name_field = QLineEdit(self)
        self.__server_name_field.setPlaceholderText('Enter the server name')
        self.__server_name_field.setFocus()
        self.__grid.addWidget(self.__server_name_field)

        # Server IP
        self.__grid.addWidget(QLabel('Server Address:', self))
        self.__server_ip_field = QLineEdit(self)
        self.__server_ip_field.setPlaceholderText('Enter the address or IP')
        self.__grid.addWidget(self.__server_ip_field)

        # Action Buttons
        self.__button_group_frame = QFrame(self)
        self.__button_group = QHBoxLayout()
        self.__button_group.setContentsMargins(0, 0, 0, 0)
        self.__button_group_frame.setLayout(self.__button_group)

        # Add Button
        self.__add_button = QPushButton('Add Server', self)
        self.__add_button.setIcon(QIcon(':world-add'))
        self.__button_group.addWidget(self.__add_button)

        # Delete Button
        self.__delete_button = QPushButton('Delete Server', self)
        self.__delete_button.setIcon(QIcon(':world-delete'))
        self.__button_group.addWidget(self.__delete_button)
        self.__grid.addWidget(self.__button_group_frame)

        # Server List
        self.__server_list = QListWidget(self)
        self.__grid.addWidget(self.__server_list)
