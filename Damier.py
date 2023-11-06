# standard library
from __future__ import annotations
import logging
import logging.config

# third-party library
import pygame

# local library
from Vaisseau import Vaisseau
from Ennemie import Ennemie


class Damier:
    def __init__(self) -> None:
        self._cases: list(list(dict)) = [[dict()
                                          for _ in range(12)] for _ in range(10)]
        self._vaisseaux: list(Vaisseau) = []
        self._ennemies: list(Ennemie) = []

        logging.info("damier initialisé")

    def deplacement(self):
        pass

    def getSize(self) -> tuple:
        return (len(self._cases), len(self._cases[0]))
