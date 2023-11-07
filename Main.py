# standard library
import logging
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
        if game.is_played:
            game.drawPlateau(screen)
            game.play_menu_in_game(screen)
        elif game.is_credit:
            game.play_credit(screen)
        else:
            game.play_menu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(40)

        pygame.display.update()

    pygame.quit()
