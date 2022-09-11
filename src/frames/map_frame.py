"""
Map frame module.
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
from models.map_model import MapModel
from services.data_service import DataService
from services.dialog_service import DialogService

from services.game_config_service import GameConfigService
from services.map_service import MapService
from services.process_service import ProcessService
if TYPE_CHECKING:
    from main_window import MainWindow


class MapFrame(QFrame):
    """
    MapFrame frame class.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new MapFrame.
        """
        super().__init__(main_window)
        self.__main_window = main_window
        self.__build()
        self.__refresh_map_list()
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
        self.__map_list.currentTextChanged.connect(
            self.__handle_map_selection
        )

    def __handle_map_selection(self, item: str) -> None:
        """
        Handle map selection event.
        """
        self.__delete_button.setDisabled(True)
        if item is None or item == '':
            return
        map_ = self.__map_row_to_map_model(item)
        if map_.val in MapService.NATIVE_MAPS:
            return
        self.__delete_button.setDisabled(False)

    def __handle_add(self) -> None:
        """
        Handle add button click event.
        """
        map_name = self.__map_name_field.text().strip()
        if len(map_name) == 0:
            DialogService.error(self, 'Invalid map name.')
            return
        map_val = self.__map_value_field.value()
        self.__map_list.addItem(
            f'{map_name}: {map_val}'
        )
        MapService.update_levels_nfo_file(
            self.__map_list_to_map_models()
        )
        self.__map_name_field.setText('')
        self.__map_value_field.setValue(1)
        self.__map_name_field.setFocus()
        self.__refresh_map_list()

    def __handle_delete(self) -> None:
        """
        Handle delete button click event.
        """
        current = self.__map_list.currentItem()
        if current is None:
            return
        selected = current.text()
        map_ = self.__map_row_to_map_model(selected)
        ok = DialogService.question(
            self,
            f'The map "{map_.name}" will be deleted. Proceed? (Note: The map' +
            ' folder will not be deleted)'
        )
        if not ok:
            return
        self.__map_list.takeItem(
            self.__map_list.currentIndex().row()
        )
        MapService.update_levels_nfo_file(
            self.__map_list_to_map_models()
        )
        self.__refresh_map_list()

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __map_list_to_map_models(self) -> list[MapModel]:
        """
        Convert map list to map models.
        """
        map_list: list[MapModel] = []
        for i in range(self.__map_list.count()):
            map = self.__map_list.item(i)
            if map is None:
                continue
            content = map.text()
            map_list.append(self.__map_row_to_map_model(content))
        return map_list

    def __map_row_to_map_model(self, map_row: str) -> MapModel:
        """
        Convert map row text to map model.
        """
        map_name, map_val = map_row.split(':')
        return MapModel(
            map_name.strip(),
            int(map_val.strip())
        )

    def __refresh_map_list(self) -> None:
        """
        Refresh map list.
        """
        self.__map_list.clear()
        maps = MapService.list_maps()
        for map_ in maps:
            self.__map_list.addItem(
                f'{map_.name}: {map_.val}'
            )
        self.__delete_button.setDisabled(True)

    def __build(self) -> None:
        """
        Build frame.
        """
        # Grid
        self.__grid = QVBoxLayout()
        self.__grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__grid)

        # Map name
        self.__grid.addWidget(QLabel('Map Name:', self))
        self.__map_name_field = QLineEdit(self)
        self.__map_name_field.setPlaceholderText(
            'Enter the server name (Ex: No Mans Land)'
        )
        self.__map_name_field.setFocus()
        self.__grid.addWidget(self.__map_name_field)

        # Map Value
        self.__grid.addWidget(QLabel('Map Value: (129 ~ 999)', self))
        self.__map_value_field = QSpinBox(self)
        self.__map_value_field.setMinimum(129)
        self.__map_value_field.setMaximum(999)
        self.__map_value_field.setValue(129)
        self.__grid.addWidget(self.__map_value_field)

        # Action Buttons
        self.__button_group_frame = QFrame(self)
        self.__button_group = QHBoxLayout()
        self.__button_group.setContentsMargins(0, 0, 0, 0)
        self.__button_group_frame.setLayout(self.__button_group)

        # Add Button
        self.__add_button = QPushButton('Add Map Record', self)
        self.__add_button.setIcon(QIcon(':map-add'))
        self.__button_group.addWidget(self.__add_button)

        # Delete Button
        self.__delete_button = QPushButton('Delete Map Record', self)
        self.__delete_button.setIcon(QIcon(':map-delete'))
        self.__button_group.addWidget(self.__delete_button)
        self.__grid.addWidget(self.__button_group_frame)

        # Server List
        self.__map_list = QListWidget(self)
        self.__grid.addWidget(self.__map_list)
