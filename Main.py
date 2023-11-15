# standard library
import logging.config

# third-party library
import pygame
# from AppKit import NSScreen, NSApplication, NSApp

# local library
from Game import Game
from Entite import Entite

logging.config.fileConfig('./conf/log-config.ini')

if __name__ == '__main__':
    pygame.init()

    screen_info = pygame.display.Info()
    dock_size = 150

    screen: pygame.Surface = pygame.display.set_mode(
        (screen_info.current_w, screen_info.current_h-dock_size))
    clock: pygame.time.Clock = pygame.time.Clock()

    game: Game = Game(screen)
    Joueur = Entite("./assets/images/VaisseauRouge.png")

    running = True
    while running:

        if game.is_joueur_set:
            if game.is_played:
                game.play_plateau(screen)
                game.play_menu_in_game(screen)
            else:
                game.play_set_nb_joueur(screen)
                game.damier.set_vaisseau(game.nb_joueur)
        elif game.is_credit:
            game.play_credit(screen)
        else:
            game.play_menu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # echap pour revenir au menu principal
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.is_played = False
                    game.is_credit = False
                    game.is_joueur_set = False
                    game.damier = Game.damier()

        clock.tick(40)

        pygame.display.update()

    pygame.quit()
