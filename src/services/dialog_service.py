"""
Dialog utilities.
"""
from typing import Any
from PyQt5.QtWidgets import QMessageBox


class DialogService:
    """
    Dialog render service.
    """

    ###########################################################################
    # Messages
    ###########################################################################

    @classmethod
    def info(self, parent: Any, message: str) -> None:
        """
        Render an information dialog.
        """
        msg = QMessageBox()
        msg.information(parent, 'Info', message)

    @classmethod
    def warning(self, parent: Any, message: str) -> None:
        """
        Render an warning dialog.
        """
        msg = QMessageBox()
        msg.warning(parent, 'Warning', message)

    @classmethod
    def error(self, parent: Any, message: str) -> None:
        """
        Render an error dialog.
        """
        msg = QMessageBox()
        msg.critical(parent, 'Error', message)

    ###########################################################################
    # Questions
    ###########################################################################

    @classmethod
    def question(self, parent: Any, message: str) -> bool:
        """
        Render a question dialog.
        """
        msg = QMessageBox()
        answer = msg.question(parent, 'Question', message)
        return True if answer == QMessageBox.Yes else False
