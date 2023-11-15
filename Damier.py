# standard library
from __future__ import annotations
import logging.config

# third-party library
# import pygame

# local library
from Vaisseau import Vaisseau
from Ennemie import Ennemie


class Damier:
    def __init__(self) -> None:
        self._cases: list(list(dict)) = [[dict()
                                          for i in range(12)] for j in range(10)]
        self._vaisseaux: list(Vaisseau) = []
        self._ennemies: list(Ennemie) = []

        logging.info("damier initialisé")

    def get_size(self) -> tuple:
        return (len(self._cases), len(self._cases[0]))

    def set_vaisseau(self, number: int) -> None:
        """
        Add a number of Vaisseau to the damier.

        Args:
            number (int): The number of Vaisseau to add.

        Returns:
            None
        """
        colors: list(str) = ["Rouge", "Bleu", "Vert", "Blanc"]
        for i in range(number):
            self._vaisseaux.append(Vaisseau(
                "./assets/images/Vaisseau" + colors[i] + ".png"))
            logging.info("vaisseau " + colors[i] + " créé")

    def deplacement(self):
        pass

    def __str__(self) -> str:
        texte: str = "[\n"
        for i in range(len(self._cases)):
            texte += "["
            for j in range(len(self._cases[i])):
                texte += f"{self._cases[i][j]}"
            texte += "]\n"
        texte += "]"
        return texte


if __name__ == "__main__":
    damier: Damier = Damier()
    print(damier)
