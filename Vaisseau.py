# standard library
from __future__ import annotations
import logging.config
from random import randint

# local library
from Entite import Entite


class Vaisseau(Entite):
    def __init__(self: Vaisseau, url: str = None, nom: str = "joueur") -> None:
        pos: tuple[int, int] = (randint(0, 11), randint(0, 9))
        super().__init__(url, nom, pos)

        # historique des mouvements du vaisseau pour un tour
        self.move_history: list[tuple[int, int]] = []

        logging.info("vaisseau initialisé avec le nom : %s", nom)

    @property
    def move_history(self: Vaisseau) -> list[tuple[int, int]]:
        return self.__move_history

    @move_history.setter
    def move_history(self: Vaisseau, move_history: list[tuple[int, int]]) -> None:
        self.__move_history = move_history


if __name__ == "__main__":
    v = Vaisseau("vaisseau")
    v.pointlife += 10
    print(v.pointlife)
