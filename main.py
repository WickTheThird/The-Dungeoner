import pygame, sys

# import settings and debug
from resource_path import debug
from settings import *
from player.player import *
from levels.level import *

# import main menu
from menu import MainMenu

class Game:
    def __init__(self):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def run(self):
        #name of game
        pygame.display.set_caption('The Doungeoner')

        #main loop
        while True:

            # event loop
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
