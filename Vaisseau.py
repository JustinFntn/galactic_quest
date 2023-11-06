from __future__ import annotations
from Entite import Entite


class Vaisseau(Entite):
    def __init__(self: Vaisseau, url: str = None, nom: str = "joueur") -> None:
        super().__init__(url, nom)

    def getcouleur(self):
        return self._couleur


if __name__ == "__main__":
    v = Vaisseau("vaisseau")
    print(v)
