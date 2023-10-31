import Entité


class Vaisseau(Entité):
    def __init__(self, nom: str, couleur: str) -> None:
        super().__init__(nom)
        self._couleur = couleur

    def getcouleur(self):
        return self._couleur


if __name__ == "__main__":
    v = Vaisseau("vaisseau")
    print(v)
