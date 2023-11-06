from __future__ import annotations
from Entite import Entite


class Ennemie(Entite):
    def __init__(self: Ennemie, nom: str = "default") -> None:
        super().__init__(nom)


if __name__ == "__main__":
    v = Ennemie("dragon")
    print(v)
