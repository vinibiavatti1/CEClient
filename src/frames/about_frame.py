from typing import TYPE_CHECKING, Any
from PyQt5.QtCore import Qt
from app_info import AppInfo
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
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
        self.__container.addWidget(QLabel(f'About {AppInfo.APP_TITLE}:', self))
        self.__text_area = QTextEdit(self)
        self.__text_area.setReadOnly(True)
        self.__text_area.setText(
            f'Application: {AppInfo.APP_TITLE} {AppInfo.APP_VERSION}\n' +
            f'Author: {AppInfo.APP_AUTHOR}\n' +
            f'Game Version: {AppInfo.GAME_NAME}\n' +
            f'CE Website: https://codenameeaglemultiplayer.com/\n' +
            f'NVL Map: https://github.com/vinibiavatti1/CodenameEagleNVLMap' +
            f'Reddit Community: https://www.reddit.com/r/CodenameEagle/\n' +
            f'Discord Community: https://discord.gg/gGaMUJA9st\n' +
            f'\n' +
            f'Please, join the Discord Community. We are waiting for you to ' +
            f'bring the CE essence again! We hope a GG for you.'
        )
        self.__container.addWidget(self.__text_area)
