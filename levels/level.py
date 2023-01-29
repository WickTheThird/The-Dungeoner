import pygame
from pygame.locals import *
from levels.map_level import Map
from player.player import Player
from settings import *
from screeninfo import get_monitors

class LevelBase:

    def __init__(self):
        # pygame setup
        pygame.init()
        
        # screen
        self.screen = None
        self.height = get_monitors()[0].height
        self.width = get_monitors()[0].width
        
        # the map
        self.map = Map().getMap()
        self.x = 0
        self.y = 0
        self.vel = 20

        # the player
        self.player = Player()
        self.state = False
    
    def drawMap(self):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = (col_index * TILESIZE)
                y = (row_index * TILESIZE)

                if col == 'x':
                    pygame.draw.rect(self.screen, (0, 0, 0), (x, y, TILESIZE, TILESIZE), 1)

    def run(self, screen, keys, image=0):

        self.screen = screen

        self.drawMap()

        if keys[K_w]:
            self.y -= 20
            self.state = True

        if keys[K_s]:
           self.y += 20
           self.state = True

        if keys[K_d]:
            self.x += 20
            self.state = True

        if keys[K_a]:
            self.x -= 20
            self.state = True

        if self.state is True and (keys[K_a] is False and keys[K_d] is False and keys[K_w] is False and keys[K_s] is False):
            self.state = False

        updatePlayer = self.player.run(screen, self.state, image)
        self.state = updatePlayer[0]
        image = updatePlayer[1]

        return image
