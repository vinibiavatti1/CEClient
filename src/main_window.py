"""
Main window module.
"""
import os
from app_info import AppInfo
from enums.frame_enum import FrameEnum
from frames.about_frame import AboutFrame
from frames.advanced_config_frame import AdvancedConfigFrame
from frames.config_frame import ConfigFrame
from frames.connection_frame import ConnectionFrame
from frames.map_frame import MapFrame
from frames.ping_test_frame import PingTestFrame
from frames.server_list_frame import ServerListFrame
from services.dialog_service import DialogService
from services.map_service import MapService
from services.path_service import PathService
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
        elif frame == FrameEnum.ADVANCED_CONFIG_FRAME:
            self.setCentralWidget(AdvancedConfigFrame(self))
        elif frame == FrameEnum.MAP_FRAME:
            self.setCentralWidget(MapFrame(self))

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
            QAction(QIcon(':joystick'), 'Game Settings', self)
        self.__server_list_config_action = \
            QAction(QIcon(':list-server'), 'Server List', self)
        self.__advanced_config_action = \
            QAction(QIcon(':config-icon'), 'Advanced Settings', self)
        self.__ping_test_action = \
            QAction(QIcon(':ping'), 'Server Ping Test', self)
        self.__about_action = \
            QAction(QIcon(':info'), 'About', self)
        self.__exit_action = \
            QAction(QIcon(':exit'), 'Exit', self)
        self.__maps_action = \
            QAction(
                QIcon(':map-edit'),
                f'Maps ({MapService.MAP_RECORDS_FILE})', self
            )
        self.__open_folder_action = \
            QAction(QIcon(':open-folder'), 'Open Game Folder...', self)
        self.__open_dg_action = \
            QAction(QIcon(':open-dg'), 'Open DgVoodoo...', self)

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
        self.__advanced_config_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.ADVANCED_CONFIG_FRAME)
        )
        self.__maps_action.triggered.connect(
            lambda: self.set_central_widget(FrameEnum.MAP_FRAME)
        )
        self.__open_folder_action.triggered.connect(
            lambda: self.handle_open_folder()
        )
        self.__open_dg_action.triggered.connect(
            lambda: self.handle_open_dg()
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
        self.__menu.addAction(self.__config_action)
        self.__menu.addAction(self.__server_list_config_action)
        self.__menu.addAction(self.__ping_test_action)
        self.__menu.addAction(self.__maps_action)
        self.__menu.addAction(self.__advanced_config_action)
        self.__menu.addAction(self.__about_action)
        self.__menu.addSeparator()
        self.__menu.addAction(self.__exit_action)
        self.__menu_bar.addMenu(self.__menu)
        self.__open_menu = QMenu('Open', self)
        self.__open_menu.addAction(self.__open_folder_action)
        self.__open_menu.addAction(self.__open_dg_action)
        self.__menu_bar.addMenu(self.__open_menu)
        self.setMenuBar(self.__menu_bar)

    def __build_status_bar(self) -> None:
        """
        Build status bar.
        """
        self.__status_bar = QStatusBar(self)
        self.__status_bar_content = QLabel(
            f'Created by: {AppInfo.APP_AUTHOR} / codenameeaglemultiplayer.com'
        )
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

    def handle_open_folder(self) -> None:
        """
        Open game folder.
        """
        os.startfile(PathService.get_game_path())

    def handle_open_dg(self) -> None:
        """
        Open DgVoodoo.
        """
        os.startfile(
            os.path.join(PathService.get_game_path(), 'dgVoodooCpl.exe')
        )
