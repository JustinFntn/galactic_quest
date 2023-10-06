from __future__ import annotations
import pygame
import Damier


class Game:
    def __init__(self, largeur: int, hauteur: int) -> None:
        # taille de l'écran d'affichage
        self.largeur_fenetre: int = largeur
        self.hauteur_fenetre: int = hauteur

        # buffer par défaut du jeu
        self.buffer = pygame.display.set_mode(
            (largeur, hauteur), pygame.SRCALPHA)
        pygame.display.set_caption("JEU")

        # chargement de l'image de fond
        self.background: pygame.Surface = pygame.image.load(
            "./assets/images/background.jpg")
        self.background = pygame.transform.scale(
            self.background, (largeur, hauteur))
        self.buffer.blit(self.background, (0, 0))

        # taille de la fenetre
        self.largeur_plateau: int = largeur-100
        self.hauteur_plateau: int = hauteur-50
        self.largeur_case: int = self.largeur_plateau/10
        self.hauteur_case: int = self.hauteur_plateau/8

        # creation de la surface de jeu du plateau
        self.plateau = pygame.Surface(
            (self.largeur_plateau, self.hauteur_plateau), pygame.SRCALPHA)

        # creation de la surface du menu
        self.menu = pygame.Surface((700, 500), pygame.SRCALPHA)

        # creation du damier de jeu
        self.damier = Damier.Damier()

        # creation de la police d'ecriture pour le menu
        self.font = pygame.font.SysFont("comicsansms", 30)

    def Menu(self: Game) -> bool:
        # dessin du titre et ajout au menu
        titre: pygame.Surface = pygame.image.load("./assets/images/titre.png")
        titre = pygame.transform.scale(titre, (700, 77))
        self.menu.blit(titre, (0, 0))

        # dessin bouton jouer et ajout au menu
        jouer: pygame.Rect = pygame.Rect(100, 150, 500, 100)
        pygame.draw.rect(self.menu, (0, 0, 0, 150), jouer)
        text: pygame.Surface = self.font.render("Jouer", True, (255, 255, 255))
        self.menu.blit(text, (100, 0))

        # affichage du menu
        position: tuple = ((self.largeur_fenetre /
                            2-350, self.hauteur_fenetre/2-250))
        self.buffer.blit(self.menu, position)
        pygame.display.update((position, (500, 500)))
        return True

    def run(self):
        clock = pygame.time.Clock()
        clock.tick(20)

        pygame.display.update(self.buffer.get_rect())
        # self.drawPlateau()
        self.Menu()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def drawCase(self, x: int, y: int):
        '''Dessine une case blanche avec des coins arrondis, aux coordonnées x et y

        Args:
            x (int): abscisse de la case
            y (int): ordonnée de la case

        Returns:
            pygame.surface: la surface où est dessinée la case
        '''
        color: tuple = (255, 255, 255, 100)
        radius: int = 25
        surface: pygame.Surface = pygame.Surface(
            (self.largeur_case, self.hauteur_case), pygame.SRCALPHA)

        # Dessiner la case avec un padding de 2px
        # Dessiner les coins arrondis
        for corner in [(2+radius, 2+radius), (self.largeur_case-radius-2, 2+radius), (self.largeur_case-radius-2, self.hauteur_case-radius-2), (2+radius, self.hauteur_case-radius-2)]:
            pygame.draw.circle(surface, color, corner, radius)

        # Dessiner les côtés
        pygame.draw.rect(surface, color, pygame.Rect(
            radius+2, 2, self.largeur_case - 2 * radius-4, self.hauteur_case-4))
        pygame.draw.rect(surface, color, pygame.Rect(
            2, radius+2, self.largeur_case-4, self.hauteur_case - 2 * radius-4))

        # ajouter la surface à la fenetre
        self.plateau.blit(surface, (x, y))

        return surface

    # def afficher_texte(self, texte, x, y, couleur):
    #     text = self.font.render(texte, True, couleur)
    #     self.fenetre.blit(text, (x, y))

    def drawPlateau(self):
        for i in range(10):
            for j in range(8):
                self.drawCase(i*self.largeur_case, j*self.hauteur_case)
        self.buffer.blit(self.plateau, (50, 25))
        pygame.display.update()
