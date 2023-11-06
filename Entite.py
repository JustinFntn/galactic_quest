# standard library
import logging
import logging.config

# third-party library
from pygame import sprite, image


class Entite(sprite.Sprite):
    def __init__(self, url: str, nom: str = "défaut") -> None:
        super().__init__()
        self._nom: str = nom
        self.image = image.load(url)
        self.rect = self.image.get_rect()
        self.rect.x = 400

    def __repr__(self) -> str:
        return self._nom
