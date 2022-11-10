"""
About frame module.
"""
from typing import TYPE_CHECKING
from PyQt5.QtCore import Qt
from app_constants import AppConstants
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QTextEdit,
)
if TYPE_CHECKING:
    from main_window import MainWindow


class AboutFrame(QFrame):
    """
    About frame.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new AboutFrame.
        """
        super().__init__(main_window)
        self._build()

    def _build(self) -> None:
        """
        Build AboutFrame.
        """
        self.__container = QVBoxLayout()
        self.__container.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__container)

        # App info
        self.__container.addWidget(
            QLabel(f'About {AppConstants.APP_TITLE}:', self)
        )
        self.__text_area = QTextEdit(self)
        self.__text_area.setReadOnly(True)
        self.__text_area.setText(
            f'Application: {AppConstants.APP_TITLE} ' +
            f'{AppConstants.APP_VERSION}\n'
            f'Author: {AppConstants.APP_AUTHOR}\n' +
            f'Game Version: {AppConstants.GAME_NAME}\n' +
            f'CE Website: {AppConstants.WEBSITE_LINK}\n' +
            f'NVL Map: {AppConstants.NVL_MAP_LINK}\n' +
            f'Reddit Community: {AppConstants.REDDIT_LINK}\n' +
            f'Discord Community: {AppConstants.DISCORD_LINK}\n' +
            f'\n' +
            f'Please, join the Discord Community. We are waiting for you to ' +
            f'bring the CE essence again! We hope a GG for you.'
        )
        self.__container.addWidget(self.__text_area)
