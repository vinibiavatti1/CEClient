import platform
from typing import TYPE_CHECKING, Any
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QTextEdit
)
import subprocess
from services.data_service import DataService
from services.dialog_service import DialogService
if TYPE_CHECKING:
    from main_window import MainWindow


class PingTestFrame(QFrame):
    """
    PingTestFrame frame.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new PingTestFrame.
        """
        super().__init__(main_window)
        self.__build()
        self.__register_handlers()
        self.__ping_test_result = ''

    def __build(self) -> None:
        """
        Build PingTestFrame.
        """
        self.__grid = QVBoxLayout()
        self.__grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.__grid)

        # Data
        data = DataService.get_data()

        # Server List
        self.__grid.addWidget(QLabel('Server List:'))
        self.__server_list = QComboBox(self)
        for server in data.server_list:
            self.__server_list.addItem(
                server['server_name'], server['server_ip']
            )
            if data.last_server_name == server['server_name']:
                self.__server_list.setCurrentText(data.last_server_name)
        self.__grid.addWidget(self.__server_list)

        # Button
        self.__test_button = QPushButton('Test Ping', self)
        self.__test_button.setIcon(QIcon(':ping'))
        if len(data.server_list) == 0:
            self.__test_button.setDisabled(True)
        self.__grid.addWidget(self.__test_button)

        # Test Result
        self.__ping_textarea = QTextEdit(self)
        self.__ping_textarea.setReadOnly(True)
        self.__grid.addWidget(self.__ping_textarea)

    ###########################################################################
    # Handlers
    ###########################################################################

    def __register_handlers(self) -> None:
        """
        Register handler events.
        """
        self.__test_button.clicked.connect(
            self.__handle_ping_test_action
        )

    def __handle_ping_test_action(self) -> None:
        """
        Ping test button action.
        """
        self.__ping_textarea.setText('')
        server_ip = self.__server_list.itemData(
            self.__server_list.currentIndex()
        )
        if ':' in server_ip:
            server_ip = str(server_ip).split(':')[0]
        # server_ip += '23'
        argument = '-n' if platform.system().lower() == "windows" else 'c'
        command = f'ping {argument} 3 {server_ip}'
        DialogService.progress(
            self,
            f'Testing ping to {server_ip} server...',
            lambda: self.__ping_test(command)
        )
        self.__ping_textarea.setText(self.__ping_test_result.strip())

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __ping_test(self, command: str) -> None:
        """
        Execute ping test.
        """
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            out, err = process.communicate()
            if out:
                self.__ping_test_result = out.decode()
            else:
                self.__ping_test_result = err.decode()
        except subprocess.CalledProcessError:
            self.__ping_test_result = 'Ping test failed'
