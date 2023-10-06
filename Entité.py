import pygame


class Entité(pygame.sprite.Sprite):
    def __init__(self, nom) -> None:
        self._nom = nom

    def __repr__(self) -> str:
        return self._nom
