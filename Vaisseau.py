# standard library
from __future__ import annotations
import logging.config

# local library
from Entite import Entite


class Vaisseau(Entite):
    def __init__(self: Vaisseau, url: str = None, nom: str = "joueur", pos: tuple = (0, 0)) -> None:
        super().__init__(url, nom, pos)

        logging.info("vaisseau initialisé avec le nom : %s", nom)


if __name__ == "__main__":
    v = Vaisseau("vaisseau")
    print(v)
