# import Vaisseau


class Damier:
    def __init__(self) -> None:
        self._cases: list(list(dict)) = [[{'test': 0}
                                          for i in range(8)] for j in range(10)]
        self._vaisseaux: list() = []

    def deplacement(self):
        pass

    def getSize(self) -> tuple:
        return (len(self._cases), len(self._cases[0]))
