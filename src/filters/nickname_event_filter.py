from typing import Any
from PyQt5 import QtCore

from services.data_service import DataService


class NicknameFilter(QtCore.QObject):
    """
    Nickname filter class.
    """

    def eventFilter(self, widget: Any, event: Any) -> bool:
        """
        Event filter impl.
        """
        if event.type() == QtCore.QEvent.FocusOut:
            nickname = widget.text()
            data = DataService.get_data()
            data.nickname = nickname
            DataService.save_data(data)
        return False
