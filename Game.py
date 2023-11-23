# standard library
from __future__ import annotations
import logging.config
import time

# third-party library
import pygame

# local library
from Damier import Damier
from Vaisseau import Vaisseau


class Game:
    def __init__(self: Game, screen: pygame.Surface) -> None:
        '''Constructeur de la classe Game.

        Args:
            self (Game): Instance de la classe Game.
            screen (pygame.Surface): Surface sur laquelle le jeu sera affiché.
        '''
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

        # nombre de joueur
        self.nb_joueur: int = 0

        # creation du damier de jeu
        self.damier = Damier()

        # variable d'état du jeu (peut-être à mettre sous forme d'enum)
        self.is_played: bool = False
        self.is_joueur_set: bool = False
        self.is_credit: bool = False
        self.is_combat: bool = False

        # variable gestion des tours
        self.tour: int = 0
        self.tour_joueur: int = 0

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
        play_button: pygame.Rect = pygame.Rect(100, 150, 500, 100)
        if play_button.collidepoint(mouse_pos[0]-position[0], mouse_pos[1]-position[1]):
            pygame.draw.rect(menu, (0, 0, 204, 150),
                             play_button, border_radius=10)
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound("./assets/sounds/lazer-sfx.mp3").play()
                self.is_joueur_set = True
                time.sleep(0.1)
        else:
            pygame.draw.rect(menu, (0, 0, 0, 150), play_button,
                             border_radius=10)

        font: pygame.font.Font = pygame.font.SysFont("comicsansms", 72)
        text: pygame.Surface = font.render("Jouer", True, (255, 255, 255))
        text_rect: pygame.Rect = text.get_rect()
        menu.blit(text, (play_button.centerx - text_rect.width /
                         2, play_button.centery - text_rect.height/2))

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

    def play_set_nb_joueur(self: Game, screen: pygame.Surface) -> None:
        '''affiche les bouttons pour la création des joueurs et retourne le nombre de joueurs.

        args:
            self (Game): Instance de la classe Game.
            screen (pygame.Surface): Surface sur laquelle le menu sera affiché.

        returns:
            int: nombre de joueur.
        '''
        # dessin du fond
        screen.blit(self.background, (0, 0))

        mouse_pos: tuple = pygame.mouse.get_pos()

        # position du menu
        position: tuple = ((self.largeur_fenetre /
                            2-350, self.hauteur_fenetre/2-250))

        # creation de la surface du menu
        menu = pygame.Surface((700, 500), pygame.SRCALPHA)

        buttons: list(pygame.Rect) = [
            pygame.Rect(0, 50, 300, 150),
            pygame.Rect(400, 50, 300, 150),
            pygame.Rect(0, 300, 300, 150),
            pygame.Rect(400, 300, 300, 150)
        ]

        font: pygame.font.Font = pygame.font.SysFont("comicsansms", 60)
        for i, button in enumerate(buttons):
            if button.collidepoint(mouse_pos[0]-position[0], mouse_pos[1]-position[1]):
                pygame.draw.rect(menu, (0, 0, 204, 150),
                                 button, border_radius=10)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.Sound("./assets/sounds/lazer-sfx.mp3").play()
                    self.is_played = True
                    self.nb_joueur = i+1
                    time.sleep(0.1)
                    return
            else:
                pygame.draw.rect(menu, (0, 0, 0, 150),
                                 button, border_radius=10)
            if i == 0:
                text: pygame.Surface = font.render(
                    "1 Joueur", True, (255, 255, 255))
            else:
                text: pygame.Surface = font.render(
                    str(i+1)+" Joueurs", True, (255, 255, 255))
            text_rect: pygame.Rect = text.get_rect()
            menu.blit(text, (button.centerx - text_rect.width /
                      2, button.centery - text_rect.height/2))

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
        color: tuple = (255, 255, 255, 100)
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

    def play_plateau(self, screen: pygame.Surface):
        '''Affiche le plateau de jeu sur l'écran donné.

        Args:
            screen (pygame.Surface): La surface d'affichage.
        '''
        screen.blit(self.background, (0, 0))

        # creation de la surface de jeu du plateau
        self.plateau = pygame.Surface(
            (self.largeur_plateau, self.hauteur_plateau), pygame.SRCALPHA)

        largeur_case: int = self.largeur_plateau/12
        hauteur_case: int = self.hauteur_plateau/10
        scale: int = int(
            largeur_case) if largeur_case < hauteur_case else int(hauteur_case)
        case: pygame.surface.Surface = self.draw_case(
            largeur_case, hauteur_case)
        for i in range(12):
            for j in range(10):
                self.plateau.blit(case, (i*largeur_case, j*hauteur_case))
                for vaisseau in self.damier._vaisseaux:
                    if vaisseau.pos == (i, j):
                        vaisseau.image = pygame.transform.scale(
                            vaisseau.image, (scale, scale))
                        self.plateau.blit(
                            vaisseau.image, (i*largeur_case, j*hauteur_case))
                for ennemie in self.damier._ennemies:
                    if ennemie.pos == (i, j):
                        ennemie.image = pygame.transform.scale(
                            ennemie.image, (scale, scale))
                        self.plateau.blit(
                            ennemie.image, (i*largeur_case, j*hauteur_case))
        screen.blit(self.plateau, (10, 10))

    def play_credit(self, screen: pygame.Surface):
        self.play_plateau(screen)

    def play_menu_in_game(self, screen: pygame.Surface):
        '''Affiche le menu de jeu dans la fenêtre de jeu.

        Args:
            screen (pygame.Surface): La surface de la fenêtre de jeu.
        '''
        # creation de la surface du menu
        largeur: int = self.largeur_fenetre-self.largeur_plateau-30
        hauteur: int = self.hauteur_plateau

        menu: pygame.Surface = pygame.Surface(
            (largeur, hauteur), pygame.SRCALPHA)
        pygame.draw.rect(menu, (100, 100, 100, 85), pygame.Rect(
            0, 0, largeur, hauteur), border_top_left_radius=20, border_top_right_radius=20)

        # affichage du titre
        titre: pygame.Surface = pygame.image.load("./assets/images/titre.png")
        titre = pygame.transform.scale(
            titre, (largeur-15, (largeur-15)*0.11))
        menu.blit(titre, (7.5, 15))

        # affichage du vaisseau du joueur courant
        current_player: pygame.Surface = pygame.image.load(
            self.damier._vaisseaux[self.tour_joueur]._url)
        current_player = pygame.transform.scale(
            current_player, (largeur, largeur))
        menu.blit(
            current_player, (0, hauteur/30))

        # affichage point de vie
        point_life: pygame.Surface = pygame.Surface(
            (largeur, hauteur/30), pygame.SRCALPHA)
        coeur: pygame.Surface = pygame.image.load(
            "./assets/images/coeur.png")
        coeur = pygame.transform.scale(
            coeur, (int(hauteur/30), int(hauteur/30)))
        mort: pygame.Surface = pygame.image.load(
            "./assets/images/mort.png")
        mort = pygame.transform.scale(mort, (int(hauteur/30), int(hauteur/30)))
        if self.damier._vaisseaux[self.tour_joueur].pointlife <= 0:
            point_life.blit(mort, (5, 0))
        elif self.damier._vaisseaux[self.tour_joueur].pointlife <= 30:
            point_life.blit(coeur, (5, 0))
            pygame.draw.rect(point_life, (255, 0, 0, 200),
                             pygame.Rect(largeur/6-5, 0, (5*largeur/6)*self.damier._vaisseaux[self.tour_joueur].pointlife/100, hauteur/30), border_radius=5)
        else:
            point_life.blit(coeur, (5, 0))
            pygame.draw.rect(point_life, (0, 255, 0, 200),
                             pygame.Rect(largeur/6-5, 0, (5*largeur/6)*self.damier._vaisseaux[self.tour_joueur].pointlife/100, hauteur/30), border_radius=5)

        menu.blit(point_life, (0, 10*hauteur/30))

        # afficher degat attaque
        attack: pygame.Surface = pygame.Surface(
            (largeur, hauteur/30), pygame.SRCALPHA)
        blaster: pygame.Surface = pygame.image.load(
            "./assets/images/blaster.png")
        width, height = blaster.get_size()
        blaster = pygame.transform.scale(
            blaster, (int(hauteur/30)+20, (int(hauteur/30)+20)*height/width))
        attack.blit(blaster, (5, 0))

        font: pygame.font.Font = pygame.font.SysFont("comicsansms", 20, True)
        text: pygame.Surface = font.render(
            f'{self.damier._vaisseaux[self.tour_joueur].attack}', True, (255, 255, 255))
        attack.blit(text, (2*largeur/6, 0))

        menu.blit(attack, (0, 12*hauteur/30))

        screen.blit(menu, (self.largeur_plateau+20, 10))
