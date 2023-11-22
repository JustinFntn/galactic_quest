# standard library
from __future__ import annotations
from typing_extensions import Self

# third-party library
from pygame import sprite, image, rect, surface


class Entite(sprite.Sprite):
    def __init__(self, url: str, nom: str = "défaut", pos: tuple[int, int] = (0, 0)) -> None:
        # initialisation du sprite, de l'image et du rectangle
        super().__init__()
        self._nom: str = nom
        self._url: str = url
        self.image: surface.Surface = image.load(url)
        self.rect: rect.Rect = self.image.get_rect()
        self.rect.x: int = 400

        self.pointlife: int = 100
        self.pos: tuple[int, int] = pos

    @property
    def pos(self: Self) -> str:
        return self._pos

    @pos.setter
    def pos(self: Self, pos: tuple[int, int]) -> None:
        self._pos = pos
