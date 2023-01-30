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
        
        # tile collision
        self.colUp = False
        self.colDown = False
        self.colRight = False
        self.colLeft = False
    
    def drawMap(self, keys):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):

                x = (col_index * TILESIZE) - self.x
                y = (row_index * TILESIZE) - self.y

                if col == 'T':

                    if self.player.playerBody().top < Rect(x, y, TILESIZE, TILESIZE).bottom:
                        self.colUp = True
                    if self.player.playerBody().top < Rect(x, y, TILESIZE, TILESIZE).bottom and keys[K_s]:
                        self.colUp = False

                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(x, y, TILESIZE, TILESIZE), 1)
            
                if col == 'B':
                    
                    if self.player.playerBody().bottom > Rect(x, y, TILESIZE, TILESIZE).top:
                        self.colDown = True
                    if self.player.playerBody().bottom > Rect(x, y, TILESIZE, TILESIZE).top and keys[K_w]:
                        self.colDown = False

                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(x, y, TILESIZE, TILESIZE), 1)
                
                if col == 'L':
                            
                    if self.player.playerBody().left < Rect(x, y, TILESIZE, TILESIZE).right:
                        self.colLeft = True
                    if self.player.playerBody().left < Rect(x, y, TILESIZE, TILESIZE).right and keys[K_d]:
                        self.colLeft = False

                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(x, y, TILESIZE, TILESIZE), 1)
            
                if col == 'R':
                    
                    if self.player.playerBody().right > Rect(x, y, TILESIZE, TILESIZE).left:
                        self.colRight = True
                    if self.player.playerBody().right > Rect(x, y, TILESIZE, TILESIZE).left and keys[K_a]:
                        self.colRight = False

                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(x, y, TILESIZE, TILESIZE), 1)

    def run(self, screen, keys, image=0):

        self.screen = screen

        self.drawMap(keys)

        if keys[K_w] and self.colUp is False:
            self.y -= 20
            self.state = True

        if keys[K_s] and self.colDown is False:
           self.y += 20
           self.state = True

        if keys[K_d] and self.colRight is False:
            self.x += 20
            self.state = True

        if keys[K_a] and self.colLeft is False:
            self.x -= 20
            self.state = True

        if self.state is True and (keys[K_a] is False and keys[K_d] is False and keys[K_w] is False and keys[K_s] is False):
            self.state = False

        updatePlayer = self.player.run(screen, self.state, image)
        self.state = updatePlayer[0]
        image = updatePlayer[1]

        return image
