"""
Dialog utilities.
"""
import threading
from typing import Any, Callable, Optional
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import Qt

class DialogService:
    """
    Dialog render service.
    """

    ###########################################################################
    # Messages
    ###########################################################################

    @classmethod
    def info(cls, parent: Any, message: str) -> None:
        """
        Render an information dialog.
        """
        msg = QMessageBox()
        msg.information(parent, 'Info', message)

    @classmethod
    def warning(cls, parent: Any, message: str) -> None:
        """
        Render an warning dialog.
        """
        msg = QMessageBox()
        msg.warning(parent, 'Warning', message)

    @classmethod
    def error(cls, parent: Any, message: str) -> None:
        """
        Render an error dialog.
        """
        msg = QMessageBox()
        msg.critical(parent, 'Error', message)

    ###########################################################################
    # Questions
    ###########################################################################

    @classmethod
    def question(cls, parent: Any, message: str) -> bool:
        """
        Render a question dialog.
        """
        msg = QMessageBox()
        answer = msg.question(parent, 'Question', message)
        return True if answer == QMessageBox.Yes else False

    ###########################################################################
    # Progress
    ###########################################################################

    @classmethod
    def progress(cls, parent: Any, message: str, action: Callable[[], None],
                 cancel_button_label: Optional[str] = None) -> None:
        """
        Show a progress bar dialog and process action in thread.
        """
        dialog = QProgressDialog(
            message, 'cancel btn', 0, 0, parent
        )
        if cancel_button_label is not None:
            dialog.setCancelButtonText(cancel_button_label)
        else:
            dialog.setCancelButton(None)
        bar = QProgressBar(dialog)
        bar.setTextVisible(False)
        bar.setMinimum(0)
        bar.setMaximum(0)
        dialog.setBar(bar)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowCloseButtonHint)
        thread = threading.Thread(target=action)
        dialog.show()
        thread.start()
        while thread.is_alive():
            QApplication.processEvents()
        dialog.close()
