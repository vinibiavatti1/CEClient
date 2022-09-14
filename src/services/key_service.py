"""
Key service module.
"""
from enums.key_enum import KeyEnum
from enums.key_name_enum import KeyNameEnum
from models.key_model import KeyModel
from services.path_service import PathService


class KeyService:
    """
    Key service.

    Fire:DIK_SPACE MOUSE_LBUTTON
    UseItem:DIK_E DIK_RETURN
    ChangeItem:DIK_Q
    DropItem:DIK_R
    Jump:DIK_LCONTROL
    Pitch+:DIK_UP MOUSE_Y
    Pitch-:DIK_DOWN MOUSE_Y
    Roll+:DIK_LEFT MOUSE_X
    Roll-:DIK_RIGHT MOUSE_X
    Forward+:DIK_W
    Forward-:DIK_S
    Yaw+:DIK_A
    Yaw-:DIK_D
    """

    @classmethod
    def update_key_file(cls, keys: dict[KeyNameEnum, KeyModel]) -> None:
        """
        Update key file by list of keyModel.
        """
        content = ''
        for k, v in keys.items():
            key1 = '' if v.key1 == KeyEnum.NONE else v.key1.name
            key2 = '' if v.key2 == KeyEnum.NONE else v.key2.name
            content += f'{k.value}:{key1} {key2}\n'
        key_conf_file = PathService.get_key_conf_path()
        with open(key_conf_file, 'w') as file:
            file.write(content)

    @classmethod
    def load_key_file(cls) -> dict[KeyNameEnum, KeyModel]:
        """
        Load key file.
        """
        key_conf_file = PathService.get_key_conf_path()
        with open(key_conf_file, 'r') as file:
            content = file.read()
        return cls.generate_key_models_by_key_conf_content(content)

    @classmethod
    def generate_key_models_by_key_conf_content(cls, content: str
        ) -> dict[KeyNameEnum, KeyModel]:
        """
        Generate a key model list by content of key conf file.
        """
        keys: dict[KeyNameEnum, KeyModel] = {}
        lines = content.split('\n')
        for line in lines:
            if line.strip() == '':
                continue
            if ':' not in line:
                continue
            name, inputs = line.split(':')
            if ' ' in inputs:
                inp1, inp2 = inputs.split(' ')
            else:
                inp1, inp2 = inputs, ''
            if not KeyNameEnum.has_value(name):
                raise Exception(f'Key {name} is not registered in application')
            if inp1 != '' and not KeyEnum.has_name(inp1):
                raise Exception(f'Key {inp1} is not registered in application')
            if inp2 != '' and not KeyEnum.has_name(inp2):
                raise Exception(f'Key {inp2} is not registered in application')
            keys[KeyNameEnum(name)] = KeyModel(
                KeyEnum.NONE if inp1 == '' else KeyEnum[inp1],
                KeyEnum.NONE if inp2 == '' else KeyEnum[inp2],
            )
        return keys
