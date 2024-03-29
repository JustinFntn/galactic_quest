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

    # à modifier car pour le moment les vaisseaux sont placés sur la même case
    move_history: list = []
    pos_joueur: tuple[int, int] = (0, 0)

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

        if game.is_played:
            pos_joueur = game.damier._vaisseaux[game.tour_joueur].pos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # echap pour revenir au menu principal
                    if event.key == pygame.K_ESCAPE:
                        game.is_played = False
                        game.is_credit = False
                        game.is_joueur_set = False
                        game = Game(screen)
                        move_history = game.damier._vaisseaux[game.tour_joueur].move_history

                    # espace pour fin de tour du joueur
                    if event.key == pygame.K_SPACE:
                        game.tour_joueur = game.tour_joueur + 1
                        game.tour = game.tour+1 if game.tour_joueur == game.nb_joueur else game.tour
                        game.tour_joueur = 0 if game.tour_joueur == game.nb_joueur else game.tour_joueur
                        move_history = []
                        print("Tour : " + str(game.tour) +
                              "\nTour joueur : " + str(game.tour_joueur))
                    if event.key == pygame.K_a:
                        game.damier._vaisseaux[game.tour_joueur].pointlife -= 10 if game.damier._vaisseaux[game.tour_joueur].pointlife > 0 else 0
                    if event.key == pygame.K_z:
                        game.damier._vaisseaux[game.tour_joueur].pointlife += 10 if game.damier._vaisseaux[game.tour_joueur].pointlife <= 90 else 0

                    # fleche pour deplacer le vaisseau
                    if event.key == pygame.K_RIGHT and len(move_history) < 3:
                        move_history.append(pos_joueur)
                        game.damier._vaisseaux[game.tour_joueur].pos = (
                            pos_joueur[0]+1, pos_joueur[1]) if pos_joueur[0] < 11 else (0, pos_joueur[1])
                    if event.key == pygame.K_LEFT and len(move_history) < 3:
                        move_history.append(pos_joueur)
                        game.damier._vaisseaux[game.tour_joueur].pos = (
                            pos_joueur[0]-1, pos_joueur[1]) if pos_joueur[0] > 0 else (11, pos_joueur[1])
                    if event.key == pygame.K_UP and len(move_history) < 3:
                        move_history.append(pos_joueur)
                        game.damier._vaisseaux[game.tour_joueur].pos = (
                            pos_joueur[0], pos_joueur[1]-1) if pos_joueur[1] > 0 else (pos_joueur[0], 9)
                    if event.key == pygame.K_DOWN and len(move_history) < 3:
                        move_history.append(pos_joueur)
                        game.damier._vaisseaux[game.tour_joueur].pos = (
                            pos_joueur[0], pos_joueur[1]+1) if pos_joueur[1] < 9 else (pos_joueur[0], 0)
                    # bouton suppression pour annuler le mouvement
                    if event.key == pygame.K_BACKSPACE:
                        if move_history:
                            game.damier._vaisseaux[game.tour_joueur].pos = move_history.pop(
                            )
        if game.is_credit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    game.is_credit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(40)

        pygame.display.update()

    pygame.quit()
