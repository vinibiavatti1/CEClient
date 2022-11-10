"""
Keys frame module.
"""
from typing import TYPE_CHECKING
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from app_constants import AppConstants
from enums.key_enum import KeyEnum
from services.dialog_service import DialogService
from services.key_service import KeyService
from PyQt5.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QTextEdit,
    QGridLayout,
    QComboBox,
    QPushButton
)
from enums.key_name_enum import KeyNameEnum

from models.key_model import KeyModel
if TYPE_CHECKING:
    from main_window import MainWindow


class KeysFrame(QFrame):
    """
    Keys frame.
    """

    def __init__(self, main_window: 'MainWindow') -> None:
        """
        Construct a new KeysFrame.
        """
        super().__init__(main_window)
        self.__build()

    ###########################################################################
    # Private Methods
    ###########################################################################

    def __build(self) -> None:
        """
        Build AboutFrame.
        """
        self.__container = QGridLayout(self)
        self.__container.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__container.setSpacing(0)
        self.setLayout(self.__container)

        try:
            keys = KeyService.load_key_file()
        except Exception as err:
            print(err)
            DialogService.error(
                self,
                f'An error ocurred to load keyconf.dat file. Error: {err}'
            )
            return

        self.fire1, self.fire2 = self.__build_key_input(
            'Fire:',
            0,
            keys[KeyNameEnum.FIRE].key1.value,
            keys[KeyNameEnum.FIRE].key2.value
        )
        self.item_vehicle1, self.item_vehicle2 = self.__build_key_input(
            'Use Item / Enter Vehicle:',
            1,
            keys[KeyNameEnum.USE_ITEM].key1.value,
            keys[KeyNameEnum.USE_ITEM].key2.value
        )
        self.change_item1, self.change_item2 = self.__build_key_input(
            'Change Item:',
            2,
            keys[KeyNameEnum.CHANGE_ITEM].key1.value,
            keys[KeyNameEnum.CHANGE_ITEM].key2.value
        )
        self.next_weapon1, self.next_weapon2 = self.__build_key_input(
            'Change Vehicle Spot:',
            3,
            keys[KeyNameEnum.DROP_ITEM].key1.value,
            keys[KeyNameEnum.DROP_ITEM].key2.value
        )
        self.jump1, self.jump2 = self.__build_key_input(
            'Jump:',
            4,
            keys[KeyNameEnum.JUMP].key1.value,
            keys[KeyNameEnum.JUMP].key2.value
        )
        self.pitch_plus1, self.pitch_plus2 = self.__build_key_input(
            'Pitch (+):',
            5,
            keys[KeyNameEnum.PITCH_PLUS].key1.value,
            keys[KeyNameEnum.PITCH_PLUS].key2.value
        )
        self.pitch_minus1, self.pitch_minus2 = self.__build_key_input(
            'Pitch (-):',
            6,
            keys[KeyNameEnum.PITCH_MINUS].key1.value,
            keys[KeyNameEnum.PITCH_MINUS].key2.value
        )
        self.roll_plus1, self.roll_plus2 = self.__build_key_input(
            'Roll (+):',
            7,
            keys[KeyNameEnum.ROLL_PLUS].key1.value,
            keys[KeyNameEnum.ROLL_PLUS].key2.value
        )
        self.roll_minus1, self.roll_minus2 = self.__build_key_input(
            'Roll (-):',
            8,
            keys[KeyNameEnum.ROLL_MINUS].key1.value,
            keys[KeyNameEnum.ROLL_MINUS].key2.value
        )
        self.forward_plus1, self.forward_plus2 = self.__build_key_input(
            'Forward (+):',
            9,
            keys[KeyNameEnum.FORWARD_PLUS].key1.value,
            keys[KeyNameEnum.FORWARD_PLUS].key2.value
        )
        self.forward_minus1, self.forward_minus2 = self.__build_key_input(
            'Forward (-):',
            10,
            keys[KeyNameEnum.FORWARD_MINUS].key1.value,
            keys[KeyNameEnum.FORWARD_MINUS].key2.value
        )
        self.yaw_plus1, self.yaw_plus2 = self.__build_key_input(
            'Yaw (+):',
            11,
            keys[KeyNameEnum.YAW_PLUS].key1.value,
            keys[KeyNameEnum.YAW_PLUS].key2.value
        )
        self.yaw_minus1, self.yaw_minus2 = self.__build_key_input(
            'Yaw (-):',
            12,
            keys[KeyNameEnum.YAW_MINUS].key1.value,
            keys[KeyNameEnum.YAW_MINUS].key2.value
        )

        # Save Button
        self.__save_button = QPushButton('Save', self)
        self.__save_button.setIcon(QIcon(':save-icon'))
        self.__container.addWidget(self.__save_button, 13, 0, 1, 3)

        # Reset to Default
        self.__reset_button = QPushButton('Reset to Default', self)
        self.__reset_button.setIcon(QIcon(':reset'))
        self.__container.addWidget(self.__reset_button, 14, 0, 1, 3)

        self.__register_handlers()

    def __build_key_input(self, label: str, row: int, value_1: str,
                          value_2: str) -> tuple[QComboBox, QComboBox]:
        """
        Build a key input.
        """
        self.__container.addWidget(
            self.__build_right_label(label), row, 0
        )
        comp1 = self.__build_key_combo_box(False)
        comp2 = self.__build_key_combo_box(True)
        comp1.setCurrentText(value_1)
        comp2.setCurrentText(value_2)
        self.__container.addWidget(comp1, row, 1)
        self.__container.addWidget(comp2, row, 2)
        return comp1, comp2

    def __build_right_label(self, text: str) -> QLineEdit:
        """
        Build right label.
        """
        comp = QLineEdit(self)
        comp.setText(text)
        comp.setReadOnly(True)
        comp.setMinimumWidth(160)
        comp.setAlignment(Qt.AlignmentFlag.AlignRight)
        return comp

    def __build_key_combo_box(self, with_blank: bool) -> QComboBox:
        """
        Create ComboBox with keys.
        """
        comp = QComboBox()
        comp.setMinimumWidth(100)
        for key in KeyEnum:
            if not with_blank and key == KeyEnum.NONE:
                continue
            comp.addItem(key.value, key.name)
        return comp

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
        self.__reset_button.clicked.connect(
            self.__handle_reset
        )

    def __handle_save(self) -> None:
        """
        Handle save button event.
        """
        keys: dict[KeyNameEnum, KeyModel] = {
            KeyNameEnum.FIRE: KeyModel(
                KeyEnum(self.fire1.currentText()),
                KeyEnum(self.fire2.currentText())
            ),
            KeyNameEnum.USE_ITEM: KeyModel(
                KeyEnum(self.item_vehicle1.currentText()),
                KeyEnum(self.item_vehicle2.currentText())
            ),
            KeyNameEnum.CHANGE_ITEM: KeyModel(
                KeyEnum(self.change_item1.currentText()),
                KeyEnum(self.change_item2.currentText())
            ),
            KeyNameEnum.DROP_ITEM: KeyModel(
                KeyEnum(self.next_weapon1.currentText()),
                KeyEnum(self.next_weapon2.currentText())
            ),
            KeyNameEnum.JUMP: KeyModel(
                KeyEnum(self.jump1.currentText()),
                KeyEnum(self.jump2.currentText())
            ),
            KeyNameEnum.PITCH_PLUS: KeyModel(
                KeyEnum(self.pitch_plus1.currentText()),
                KeyEnum(self.pitch_plus2.currentText())
            ),
            KeyNameEnum.PITCH_MINUS: KeyModel(
                KeyEnum(self.pitch_minus1.currentText()),
                KeyEnum(self.pitch_minus2.currentText())
            ),
            KeyNameEnum.ROLL_PLUS: KeyModel(
                KeyEnum(self.roll_plus1.currentText()),
                KeyEnum(self.roll_plus2.currentText())
            ),
            KeyNameEnum.ROLL_MINUS: KeyModel(
                KeyEnum(self.roll_minus1.currentText()),
                KeyEnum(self.roll_minus2.currentText())
            ),
            KeyNameEnum.FORWARD_PLUS: KeyModel(
                KeyEnum(self.forward_plus1.currentText()),
                KeyEnum(self.forward_plus2.currentText())
            ),
            KeyNameEnum.FORWARD_MINUS: KeyModel(
                KeyEnum(self.forward_minus1.currentText()),
                KeyEnum(self.forward_minus2.currentText())
            ),
            KeyNameEnum.YAW_PLUS: KeyModel(
                KeyEnum(self.yaw_plus1.currentText()),
                KeyEnum(self.yaw_plus2.currentText())
            ),
            KeyNameEnum.YAW_MINUS: KeyModel(
                KeyEnum(self.yaw_minus1.currentText()),
                KeyEnum(self.yaw_minus2.currentText())
            ),
        }
        KeyService.update_key_file(keys)
        DialogService.info(
            self,
            'Key configuration saved successfully!'
        )

    def __handle_reset(self) -> None:
        """
        Reset keys to default.
        """
        ok = DialogService.question(
            self,
            'The keys will reset to default configuration. Proceed?'
        )
        if not ok:
            return
        self.fire1.setCurrentText(KeyEnum.DIK_SPACE.value)
        self.fire2.setCurrentText(KeyEnum.MOUSE_LBUTTON.value)
        self.item_vehicle1.setCurrentText(KeyEnum.DIK_E.value)
        self.item_vehicle2.setCurrentText(KeyEnum.DIK_RETURN.value)
        self.change_item1.setCurrentText(KeyEnum.DIK_Q.value)
        self.change_item2.setCurrentText(KeyEnum.NONE.value)
        self.next_weapon1.setCurrentText(KeyEnum.DIK_R.value)
        self.next_weapon2.setCurrentText(KeyEnum.NONE.value)
        self.jump1.setCurrentText(KeyEnum.DIK_LCONTROL.value)
        self.jump2.setCurrentText(KeyEnum.NONE.value)
        self.pitch_plus1.setCurrentText(KeyEnum.DIK_UP.value)
        self.pitch_plus2.setCurrentText(KeyEnum.MOUSE_Y.value)
        self.pitch_minus1.setCurrentText(KeyEnum.DIK_DOWN.value)
        self.pitch_minus2.setCurrentText(KeyEnum.MOUSE_Y.value)
        self.roll_plus1.setCurrentText(KeyEnum.DIK_LEFT.value)
        self.roll_plus2.setCurrentText(KeyEnum.MOUSE_X.value)
        self.roll_minus1.setCurrentText(KeyEnum.DIK_RIGHT.value)
        self.roll_minus2.setCurrentText(KeyEnum.MOUSE_X.value)
        self.forward_plus1.setCurrentText(KeyEnum.DIK_W.value)
        self.forward_plus2.setCurrentText(KeyEnum.NONE.value)
        self.forward_minus1.setCurrentText(KeyEnum.DIK_S.value)
        self.forward_minus2.setCurrentText(KeyEnum.NONE.value)
        self.yaw_plus1.setCurrentText(KeyEnum.DIK_A.value)
        self.yaw_plus2.setCurrentText(KeyEnum.NONE.value)
        self.yaw_minus1.setCurrentText(KeyEnum.DIK_D.value)
        self.yaw_minus2.setCurrentText(KeyEnum.NONE.value)
