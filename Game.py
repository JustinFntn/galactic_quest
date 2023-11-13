# standard library
from __future__ import annotations
import logging
import logging.config
import time

# third-party library
import pygame

# local library
from Damier import Damier

logging.config.fileConfig('./conf/log-config.ini')


class Game:
    def __init__(self: Game, screen: pygame.Surface) -> None:
        # taille de l'écran d'affichage
        self.largeur_fenetre: int = screen.get_width()
        self.hauteur_fenetre: int = screen.get_height()

        # initialisation du nom de la fenetre
        pygame.display.set_caption("Galactic Quest")

        # chargement de l'image de fond
        self.background: pygame.Surface = pygame.image.load(
            "./assets/images/background2.jpg")
        self.background = pygame.transform.scale(
            self.background, (self.largeur_fenetre, self.hauteur_fenetre))

        # taille de la fenetre
        self.largeur_plateau: int = self.largeur_fenetre-300
        self.hauteur_plateau: int = self.hauteur_fenetre-20

        # creation du damier de jeu
        self.damier = Damier()

        # variable d'état du jeu (peut-être à mettre sous forme d'enum)
        self.is_played: bool = False
        self.is_credit: bool = False

        logging.info("jeu initialisé")

    def play_menu(self: Game, screen: pygame.Surface) -> None:
        """
        Affiche le menu principal du jeu et gère les événements liés à ce menu.

        Args:
            self (Game): Instance de la classe Game.
            screen (pygame.Surface): Surface sur laquelle le menu sera affiché.

        Returns:
            None
        """
        # dessin du fond
        screen.blit(self.background, (0, 0))

        mouse_pos: tuple = pygame.mouse.get_pos()

        # creation de la surface du menu
        menu = pygame.Surface((700, 500), pygame.SRCALPHA)

        # position du menu
        position: tuple = ((self.largeur_fenetre /
                            2-350, self.hauteur_fenetre/2-250))

        # dessin du titre et ajout au menu
        titre: pygame.Surface = pygame.image.load("./assets/images/titre.png")
        titre = pygame.transform.scale(titre, (700, 77))
        menu.blit(titre, (0, 0))

        # dessin bouton jouer et ajout au menu (avec gestion des événements)
        self.jouer: pygame.Rect = pygame.Rect(100, 150, 500, 100)
        if self.jouer.collidepoint(mouse_pos[0]-position[0], mouse_pos[1]-position[1]):
            pygame.draw.rect(menu, (0, 0, 204, 150),
                             self.jouer, border_radius=10)
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound("./assets/sounds/lazer-sfx.mp3").play()
                self.is_played = True
                time.sleep(0.1)
        else:
            pygame.draw.rect(menu, (0, 0, 0, 150), self.jouer,
                             border_radius=10)

        font: pygame.font.Font = pygame.font.SysFont("comicsansms", 72)
        text: pygame.Surface = font.render("Jouer", True, (255, 255, 255))
        text_rect: pygame.Rect = text.get_rect()
        menu.blit(text, (self.jouer.centerx - text_rect.width /
                         2, self.jouer.centery - text_rect.height/2))

        # dessin bouton crédits et ajout au menu (avec gestion des événements)
        credit: pygame.Rect = pygame.Rect(100, 300, 500, 100)
        if credit.collidepoint(mouse_pos[0]-position[0], mouse_pos[1]-position[1]):
            pygame.draw.rect(menu, (0, 0, 204, 150), credit, border_radius=10)
            if pygame.mouse.get_pressed()[0]:
                self.is_credit = True
        else:
            pygame.draw.rect(menu, (0, 0, 0, 150), credit, border_radius=10)

        text: pygame.Surface = font.render("Crédits", True, (255, 255, 255))
        text_rect: pygame.Rect = text.get_rect()
        menu.blit(text, (credit.centerx - text_rect.width /
                         2, credit.centery - text_rect.height/2))

        # dessin du menu
        screen.blit(menu, position)

    def draw_case(self: Game, largeur_case: int, hauteur_case: int) -> pygame.Surface:
        '''Dessine une case avec coins arrondis et retourne la surface pygame correspondante.

        Args:
            self (Game): Instance de la classe Game.
            largeur_case (int): Largeur de la case à dessiner.
            hauteur_case (int): Hauteur de la case à dessiner.

        Returns:
            pygame.Surface: Surface pygame correspondant à la case dessinée.
        '''
        color: tuple = (255, 255, 255, 75)
        radius: int = 25 if largeur_case > 50 else 0
        surface: pygame.Surface = pygame.Surface(
            (largeur_case, hauteur_case), pygame.SRCALPHA)

        # Dessiner la case avec le padding
        # 1ere étape les coins arrondis
        for corner in [(2+radius, 2+radius), (largeur_case-radius-2, 2+radius), (largeur_case-radius-2, hauteur_case-radius-2), (2+radius, hauteur_case-radius-2)]:
            pygame.draw.circle(surface, color, corner, radius)

        # 2eme étapes les côtés
        pygame.draw.rect(surface, color, pygame.Rect(
            radius+2, 2, largeur_case - 2 * radius-4, hauteur_case-4))
        pygame.draw.rect(surface, color, pygame.Rect(
            2, radius+2, largeur_case-4, hauteur_case - 2 * radius-4))

        return surface

    # def afficher_texte(self, texte, x, y, couleur):
    #     text = self.font.render(texte, True, couleur)
    #     self.fenetre.blit(text, (x, y))

    def draw_plateau(self, screen: pygame.Surface):
        screen.blit(self.background, (0, 0))

        # creation de la surface de jeu du plateau
        self.plateau = pygame.Surface(
            (self.largeur_plateau, self.hauteur_plateau), pygame.SRCALPHA)

        largeur_case = self.largeur_plateau/12
        hauteur_case = self.hauteur_plateau/10
        case: pygame.surface.Surface = self.draw_case(
            largeur_case, hauteur_case)
        for i in range(12):
            for j in range(10):
                self.plateau.blit(case, (i*largeur_case, j*hauteur_case))

        screen.blit(self.plateau, (10, 10))

    def play_credit(self, screen: pygame.Surface):
        self.draw_plateau(screen)

    def play_menu_in_game(self, screen: pygame.Surface):
        largeur: int = self.largeur_fenetre-self.largeur_plateau-30
        hauteur: int = self.hauteur_plateau

        menu: pygame.Surface = pygame.Surface(
            (largeur, hauteur), pygame.SRCALPHA)
        pygame.draw.rect(menu, (100, 100, 100, 85), pygame.Rect(
            0, 0, largeur, hauteur), border_top_left_radius=20, border_top_right_radius=20)

        titre: pygame.Surface = pygame.image.load("./assets/images/titre.png")
        titre = pygame.transform.scale(
            titre, (largeur-15, (largeur-15)*0.11))
        menu.blit(titre, (7.5, 15))

        screen.blit(menu, (self.largeur_plateau+20, 10))

    def __str__(self: Game) -> str:
        json: str = "{\n"
        json += f"\t\"largeur_fenetre\": {self.largeur_fenetre},\n"
        json += f"\t\"hauteur_fenetre\": {self.hauteur_fenetre},\n"
        json += f"\t\"largeur_plateau\": {self.largeur_plateau},\n"
        json += f"\t\"hauteur_plateau\": {self.hauteur_plateau},\n"
        json += f"\t\"damier\": {self.damier}\n"
        json += "}"
        return json
