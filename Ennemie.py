from __future__ import annotations
import Entité


class Ennemie(Entité):
    def __init__(self: Ennemie, nom: str) -> None:
        super().__init__(nom)


if __name__ == "__main__":
    v = Ennemie("dragon")
    print(v)
