"""
Config frame module.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from typing import TYPE_CHECKING
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QSpinBox,
)
from enums.frame_enum import FrameEnum
from frames.connection_frame import ConnectionFrame
from services.data_service import DataService

from services.game_config_service import GameConfigService
if TYPE_CHECKING:
    from main_window import MainWindow


class ConfigFrame(QFrame):
    """
    Config frame class.
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

    def __handle_save(self) -> None:
        """
        Handle save button click.
        """
        fov = self.__fov_field.value()
        mousesens = self.__mousesens_field.value()
        viewdist = self.__viewdist_field.value()
        latency = self.__latency_field.value()
        GameConfigService.save_game_configuration(
            fov, mousesens, viewdist, latency
        )
        data = DataService.get_data()
        data.fov = fov
        data.mousesens = mousesens
        data.viewdist = viewdist
        data.latency = latency
        DataService.save_data(data)
        self.__main_window.set_central_widget(
            FrameEnum.CONNECTION_FRAME
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

        # Fov
        self.__grid.addWidget(QLabel(
            f'Field of View (fov) (100 ~ 500) ' +
            f'(Default: {GameConfigService.DEFAULT_FOV}):', self
        ))
        self.__fov_field = QSpinBox(self)
        self.__fov_field.setMinimum(100)
        self.__fov_field.setMaximum(500)
        self.__fov_field.setValue(data.fov)
        self.__grid.addWidget(self.__fov_field)

        # Mouse Sensitivity
        self.__grid.addWidget(QLabel(
            f'Mouse Sensitivity (mousesens) (1 ~ 20) ' +
            f'(Default: {GameConfigService.DEFAULT_MOUSE_SENS}):', self
        ))
        self.__mousesens_field = QSpinBox(self)
        self.__mousesens_field.setMinimum(1)
        self.__mousesens_field.setMaximum(20)
        self.__mousesens_field.setValue(data.mousesens)
        self.__grid.addWidget(self.__mousesens_field)

        # View Dist
        self.__grid.addWidget(QLabel(
            f'View Distance (viewdist) (100 ~ 5000) ' +
            f'(Default: {GameConfigService.DEFAULT_VIEWDIST}):', self
        ))
        self.__viewdist_field = QSpinBox(self)
        self.__viewdist_field.setMinimum(100)
        self.__viewdist_field.setMaximum(5000)
        self.__viewdist_field.setValue(data.viewdist)
        self.__grid.addWidget(self.__viewdist_field)

        # Latency
        self.__grid.addWidget(QLabel(
            f'Latency (latency) (0 ~ 8) ' +
            f'(Default: {GameConfigService.DEFAULT_LATENCY}):', self
        ))
        self.__latency_field = QSpinBox(self)
        self.__latency_field.setMinimum(0)
        self.__latency_field.setMaximum(16)
        self.__latency_field.setValue(data.latency)
        self.__grid.addWidget(self.__latency_field)

        # Save button
        self.__save_button = QPushButton('Save', self)
        self.__save_button.setIcon(QIcon(':save-icon'))
        self.__grid.addWidget(self.__save_button)
