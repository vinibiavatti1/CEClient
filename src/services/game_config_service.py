"""
Game configuration module to work with default.cfg file.
"""
from services.path_service import PathService


class GameConfigService:
    """
    Game configuration service.
    """

    DEFAULT_FOV: int = 200
    DEFAULT_MOUSE_SENS: int = 9
    DEFAULT_LATENCY: int = 0
    DEFAULT_VIEWDIST: int = 3000

    @classmethod
    def save_game_configuration(cls, fov: int, mousesens: int, viewdist: int,
                                latency: int) -> None:
        """
        Save game configuration to default.cfg.
        """
        game_configuration = cls.generate_default_cfg_content(
            fov, mousesens, viewdist, latency
        )
        with open(PathService.get_default_cfg_path(), 'w+') as file:
            file.write(game_configuration)

    @classmethod
    def generate_default_cfg_content(cls, fov: int, mousesens: int,
                                     viewdist: int, latency: int) -> str:
        """
        Generate default cfg configuration content.
        """
        content: list[str] = []
        content.append(f'fov {fov}')
        content.append(f'mousesens {mousesens}')
        content.append(f'latency {latency}')
        content.append(f'viewdist {viewdist}')
        return '\n'.join(content)
