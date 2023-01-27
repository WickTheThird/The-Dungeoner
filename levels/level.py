import pygame
from pygame.locals import *
from levels.map_level import Map
from player.player import Player
from settings import *

class LevelBase:

    def __init__(self):
        # pygame setup
        pygame.init()
        
        # the map
        self.map = Map()
        
        # the player
        self.player = Player()

    def run(self, screen, changeX, changeY):

        for row_index, row in enumerate(self.map.getMap()):
               for col_index, col in enumerate(row):
                    x = (col_index * TILESIZE) + ( -1 * changeX)
                    y = (row_index * TILESIZE) +( -1 * changeY)
                
                    if col == 'x':
                        pygame.draw.rect(screen, (255, 0, 0), Rect((x, y), (TILESIZE, TILESIZE)), 1) # <-- testing
