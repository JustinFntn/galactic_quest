import pygame
import Game

if __name__ == '__main__':
    pygame.init()
    game: Game = Game.Game(1300, 800)
    game.run()
