# standard library
from __future__ import annotations
from typing_extensions import Self

# third-party library
from pygame import sprite, image, rect, surface


class Entite(sprite.Sprite):
    def __init__(self, url: str, nom: str = "défaut", pos: tuple[int, int] = (0, 0)) -> None:
        '''Classe représentant une entité dans le jeu.

        Args:
            url (str): L'URL de l'image de l'entité.
            nom (str, optional): Le nom de l'entité (par défaut "défaut").
            pos (tuple[int, int], optional): La position initiale de l'entité (par défaut (0, 0))..
        '''
        super().__init__()
        self._nom: str = nom
        self._url: str = url
        try:
            self.image: surface.Surface = image.load(url)
            self.rect: rect.Rect = self.image.get_rect()
            self.rect.x: int = 400
        except:
            print("erreur lors du chargement de l'image")

        self.__pointlife: int = 100
        self.__attack: int = 10
        self.__pos: tuple[int, int] = pos

    @property
    def pointlife(self: Self) -> str:
        '''Getter pour le nombre de points de vie de l'entité.

        Returns:
            str: Le nombre de points de vie de l'entité.
        '''
        return self.__pointlife

    @pointlife.setter
    def pointlife(self: Self, pointlife: int) -> None:
        '''Setter pour le nombre de points de vie de l'entité.

        Args:
            pointlife (int): Le nouveau nombre de points de vie de l'entité.
        '''
        self.__pointlife = pointlife

    @property
    def attack(self: Self) -> str:
        '''Getter pour la force d'attaque de l'entité.

        Returns:
            str: La force d'attaque de l'entité.
        '''
        return self.__attack

    @attack.setter
    def attack(self: Self, attack: int) -> None:
        '''Setter pour la force d'attaque de l'entité.

        Args:
            attack (int): La nouvelle force d'attaque de l'entité.
        '''
        self.__attack = attack

    @property
    def pos(self: Self) -> str:
        '''Getter pour la position de l'entité.

        Returns:
            str: La position de l'entité.
        '''
        return self.__pos

    @pos.setter
    def pos(self: Self, pos: tuple[int, int]) -> None:
        """
        Setter pour la position de l'entité.

        :param pos: La nouvelle position de l'entité.
        """
        self.__pos = pos
