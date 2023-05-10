import pygame, sys

#? import settings and debug
from resource_path import debug
from settings import *
#? player
from player.player import Player
#? map_gen
from map_gen.level import LevelBase
from map_gen.map_level import Map
#? main.py
from menu import MainMenu

class Game:
    def __init__(self):
        #> pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        #> maps
        self.map = Map(width=1000, height=1000, scale=10, octaves=4)

        #> level
        self.level = LevelBase()

    def run(self):
        #> name of game
        pygame.display.set_caption('The Doungeoner')

        #> main loop
        while True:

            #> event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_l):
                    pygame.quit()
                    sys.exit()

            #> draw map
            self.map.draw_map(self.screen)

            #> update display
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
