# standard library

# third-party library
from pygame import sprite, image, rect, surface


class Entite(sprite.Sprite):
    def __init__(self, url: str, nom: str = "défaut", pos: tuple = (0, 0)) -> None:
        # initialisation du sprite, de l'image et du rectangle
        super().__init__()
        self._nom: str = nom
        self.image: surface.Surface = image.load(url)
        self.rect: rect.Rect = self.image.get_rect()
        self.rect.x: int = 400

        self.pointlife: int = 100
        self.pos: tuple = pos

    def __repr__(self) -> str:
        return self._nom
