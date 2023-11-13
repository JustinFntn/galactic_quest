# standard library
from __future__ import annotations
import logging.config

# local library
from Entite import Entite


class Ennemie(Entite):
    def __init__(self: Ennemie, nom: str = "default") -> None:
        super().__init__(nom)

        logging.info("ennemie initialisé avec le nom : %s", nom)


if __name__ == "__main__":
    v = Ennemie("dragon")
    print(v)
