"""
Main window module.
"""
from app_info import AppInfo
from enums.frame_enum import FrameEnum
from frames.about_frame import AboutFrame
from frames.config_frame import ConfigFrame
from frames.connection_frame import ConnectionFrame
from frames.ping_test_frame import PingTestFrame
from frames.server_list_frame import ServerListFrame
from services.dialog_service import DialogService
from typing import Any
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QStatusBar,
)
import qrc_resources


class MainWindow(QMainWindow):
    """
    Main window class.
    """

    def __init__(self, parent: Any = None) -> None:
        """
        Construct a new MainWindow.
        """
        super().__init__(parent)
        self.setWindowIcon(QIcon(':ce-icon'))
        self.resize(460, 360)
        self.setWindowTitle(f'{AppInfo.APP_TITLE} {AppInfo.APP_VERSION}')
        self.__register_actions()
        self.__build_menu()
        self.__build_status_bar()
        self.__register_handlers()
        self.setCentralWidget(ConnectionFrame(self))

    ###########################################################################
    # Public Methods
    ###########################################################################

    def set_central_widget(self, frame: FrameEnum) -> None:
        """
        Set the central widget to show in the window.
        """
        if frame == FrameEnum.CONNECTION_FRAME:
            self.setCentralWidget(ConnectionFrame(self))
        elif frame == FrameEnum.CONFIG_FRAME:
            self.setCentralWidget(ConfigFrame(self))
        elif frame == FrameEnum.SERVER_LIST_FRAME:
            self.setCentralWidget(ServerListFrame(self))
        elif frame == FrameEnum.ABOUT_FRAME:
            self.setCentralWidget(AboutFrame(self))
        elif frame == FrameEnum.PING_TEST_FRAME:
            self.setCentralWidget(PingTestFrame(self))

    ###########################################################################
    # Registrations
    ###########################################################################

    def __register_actions(self) -> None:
        """
        Register window actions.
        """
        self.__connection_action = \
            QAction(QIcon(':world-icon'), 'Game Connection', self)
        self.__config_action = \
            QAction(QIcon(':config-icon'), 'Game Configuration', self)
        self.__server_list_config_action = \
            QAction(QIcon(':config-icon'), 'Server List Configuration', self)
        self.__ping_test_action = \
            QAction(QIcon(':ping'), 'Server Ping Test', self)
        self.__about_action = \
            QAction(QIcon(':info'), 'About', self)
        self.__exit_action = \
            QAction(QIcon(':exit'), 'Exit', self)

    def __register_handlers(self) -> None:
        """
        Register handlers.
        """
        self.__connection_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.CONNECTION_FRAME)
        )
        self.__config_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.CONFIG_FRAME)
        )
        self.__server_list_config_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.SERVER_LIST_FRAME)
        )
        self.__about_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.ABOUT_FRAME)
        )
        self.__ping_test_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.PING_TEST_FRAME)
        )
        self.__exit_action.triggered.connect(
            self.exit_action_handler
        )

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __build_menu(self) -> None:
        """
        Build top menu.
        """
        self.__menu_bar = QMenuBar(self)
        self.__menu = QMenu('Menu', self)
        self.__menu.addAction(self.__connection_action)
        self.__menu.addSeparator()
        self.__menu.addAction(self.__config_action)
        self.__menu.addAction(self.__server_list_config_action)
        self.__menu.addAction(self.__ping_test_action)
        self.__menu.addSeparator()
        self.__menu.addAction(self.__about_action)
        self.__menu.addAction(self.__exit_action)
        self.__menu_bar.addMenu(self.__menu)
        self.setMenuBar(self.__menu_bar)

    def __build_status_bar(self) -> None:
        """
        Build status bar.
        """
        self.__status_bar = QStatusBar(self)
        self.__status_bar_content = QLabel(f'Created by: {AppInfo.APP_AUTHOR}')
        self.__status_bar.addPermanentWidget(self.__status_bar_content, 100)
        self.setStatusBar(self.__status_bar)

    ###########################################################################
    # Handlers
    ###########################################################################

    def exit_action_handler(self) -> None:
        """
        Exit the application.
        """
        ok = DialogService.question(self, 'Do you really want to quit?')
        if ok:
            self.close()
