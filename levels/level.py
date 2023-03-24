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
        self.map = Map()
        self.x = 0
        self.y = 0

        # the player
        self.player = Player()
        self.state = False
    
    def Borders(self):
        map = self.map.getMap()
        
        for rowInd, row in enumerate(map):
            for colInd, col in enumerate(row):
                
                x = (colInd * TILESIZE) - self.x
                y = (rowInd * TILESIZE) - self.y
                
                if col == 'LT' or col == 'LR' or col == 'LL' or col == 'LB':
                    pygame.draw.rect(self.screen, (0,0,0), (x, y, TILESIZE, TILESIZE))
    
    def Center(self):
        room = self.map.mainChamber()

    def run(self, screen, keys, image=0):

        self.screen = screen

        self.Borders()

        if keys[K_w]:
            self.y -= 20
            self.state = True

        if keys[K_s]:
           self.y += 20
           self.state = True

        if keys[K_d]:
            self.x += 20
            self.state = True

        if keys[K_a] :
            self.x -= 20
            self.state = True

        if self.state is True and (keys[K_a] is False and keys[K_d] is False and keys[K_w] is False and keys[K_s] is False):
            self.state = False

        updatePlayer = self.player.run(screen, self.state, image)
        self.state = updatePlayer[0]
        image = updatePlayer[1]

        return image
