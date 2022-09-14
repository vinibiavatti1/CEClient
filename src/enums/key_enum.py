"""
Keyboard keys enumeration.
"""
from enum import Enum


class KeyEnum(Enum):
    """
    Keys enum.
    """

    # None
    NONE = ''

    # Mouse
    MOUSE_Y = 'Mouse Y'
    MOUSE_X = 'Mouse X'
    MOUSE_RIGHT = 'Mouse Right'
    MOUSE_LBUTTON = 'Mouse Left Button'
    MOUSE_RBUTTON = 'Mouse Right Button'

    # Numbers
    DIK_0 = '0'
    DIK_1 = '1'
    DIK_2 = '2'
    DIK_3 = '3'
    DIK_4 = '4'
    DIK_5 = '5'
    DIK_6 = '6'
    DIK_7 = '7'
    DIK_8 = '8'
    DIK_9 = '9'

    # Letters
    DIK_A = 'A'
    DIK_B = 'B'
    DIK_C = 'C'
    DIK_D = 'D'
    DIK_E = 'E'
    DIK_F = 'F'
    DIK_G = 'G'
    DIK_H = 'H'
    DIK_I = 'I'
    DIK_J = 'J'
    DIK_K = 'K'
    DIK_L = 'L'
    DIK_M = 'M'
    DIK_N = 'N'
    DIK_O = 'O'
    DIK_P = 'P'
    DIK_Q = 'Q'
    DIK_R = 'R'
    DIK_S = 'S'
    DIK_T = 'T'
    DIK_U = 'U'
    DIK_V = 'V'
    DIK_W = 'W'
    DIK_X = 'X'
    DIK_Y = 'Y'
    DIK_Z = 'Z'

    # Controls
    DIK_LCONTROL = 'Left Control'
    DIK_RCONTROL = 'Right Control'

    # Alts
    DIK_LMENU = 'Left Alt'
    DIK_RMENU = 'Right Alt'

    # Shifts
    DIK_LSHIFT = 'Left Shift'
    DIK_RSHIFT = 'Right Shift'

    # Win keys
    DIK_LWIN = 'Left Windows Key'
    DIK_RWIN = 'Right Windows Key'

    # Function keys
    DIK_F1 = 'F1'
    DIK_F2 = 'F2'
    DIK_F3 = 'F3'
    DIK_F4 = 'F4'
    DIK_F5 = 'F5'
    DIK_F6 = 'F6'
    DIK_F7 = 'F7'
    DIK_F8 = 'F8'
    DIK_F9 = 'F9'
    DIK_F10 = 'F10'
    DIK_F11 = 'F11'
    DIK_F12 = 'F12'
    DIK_F13 = 'F13'
    DIK_F14 = 'F14'
    DIK_F15 = 'F15'

    # Numpad
    DIK_NUMLOCK = 'Numpad Lock'
    DIK_NUMPAD0 = 'Numpad 0'
    DIK_NUMPAD1 = 'Numpad 1'
    DIK_NUMPAD2 = 'Numpad 2'
    DIK_NUMPAD3 = 'Numpad 3'
    DIK_NUMPAD4 = 'Numpad 4'
    DIK_NUMPAD5 = 'Numpad 5'
    DIK_NUMPAD6 = 'Numpad 6'
    DIK_NUMPAD7 = 'Numpad 7'
    DIK_NUMPAD8 = 'Numpad 8'
    DIK_NUMPAD9 = 'Numpad 9'
    DIK_NUMPADENTER = 'Numpad Return (Enter)'
    DIK_NUMPADCOMMA = 'Numpad Comma (,)'
    DIK_DECIMAL = 'Numpad Decimal (.)'
    DIK_ADD = 'Numpad Plus (+)'
    DIK_SUBTRACT = 'Numpad Subtract (-)'
    DIK_MULTIPLY = 'Numpad Multiply (*)'
    DIK_DIVIDE = 'Numpad Divide (/)'
    DIK_NUMPADEQUALS = 'Numpad Equals (=)'

    # Arrows
    DIK_UP = 'Up Arrow'
    DIK_DOWN = 'Down Arrow'
    DIK_LEFT = 'Left Arrow'
    DIK_RIGHT = 'Right Arrow'

    # Nav
    DIK_HOME = 'Home'
    DIK_END = 'End'
    DIK_INSERT = 'Insert (Ins)'
    DIK_DELETE = 'Delete (Del)'
    DIK_PRIOR = 'Page Up (PgUp)'
    DIK_NEXT = 'Page Down (PgDn)'

    # Keyboard Math
    DIK_MINUS = 'Minus (-)'
    DIK_EQUALS = 'Equals (=)'

    # Tab
    DIK_TAB = 'Tab'

    # Brackets
    DIK_LBRACKET = 'Left Bracket'
    DIK_RBRACKET = 'Right Bracket'

    # General
    DIK_ESCAPE = 'Escape (Esc)'
    DIK_BACK = 'Backspace'
    DIK_RETURN = 'Return (Enter)'
    DIK_SPACE = 'Space'

    # Other
    DIK_SEMICOLON = 'Semicolon (;)'
    DIK_APOSTROPHE = 'Apostrophe (\')'
    DIK_GRAVE = 'Grave (`)'
    DIK_BACKSLASH = 'Back Slash (\)'
    DIK_COMMA = 'Comma (,)'
    DIK_PERIOD = 'Period (.)'
    DIK_SLASH = 'Slash (/)'
    DIK_CAPITAL = 'Capital'
    DIK_SCROLL = 'Scroll Lock'
    DIK_SYSRQ = 'SysRq'
    DIK_AT = 'At'
    DIK_COLON = 'Colon'
    DIK_UNDERLINE = 'Underline'
    DIK_STOP = 'Stop'
    DIK_APPS = 'Apps'

    @classmethod
    def has_name(cls, name: str) -> bool:
        """
        Validates if enum contains name.
        """
        return name in cls.__members__
