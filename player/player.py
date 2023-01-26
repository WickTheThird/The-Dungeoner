import pygame
from pygame.locals import *

import pygame, sys

# import settings and debug
from resource_path import debug
from settings import *
from screeninfo import get_monitors

class Player:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()

        #path to player animation
        self.player_idle = 'graphics/player/knight_f_idle_anim_f' # note that an int must go after this 
                                                                  # max is 3 (for idle)
        # screen size
        self.height = get_monitors()[0].height
        self.width = get_monitors()[0].width

        # declaring play state
        self.load_player = False

        # declaring movement
        self.move = False
        self.x = 0
        self.y = 0

        # declaring collision states
        self.player_body = None

    def idle_player_move(self, image=0):

        file = self.player_idle + str(image) + '.png'

        idle_player = pygame.image.load(file).convert_alpha()
        idle_player = pygame.transform.scale(idle_player, (32, 56))

        return idle_player
    
    def run(self, screen, keys, image=0):
        # manage the animation
        self.clock.tick(25)

        # movement
        if keys[K_w]:
            self.y -= 20
            self.move = True

        if keys[K_s]:
           self.y += 20
           self.move = True

        if keys[K_d]:
            self.x += 20
            self.move = True

        if keys[K_a]:
            self.x -= 20
            self.move = True

        if self.move is True and (keys[K_a] is False and keys[K_d] is False and keys[K_w] is False and keys[K_s] is False):
            self.move = False

        if self.move is True:
            screen.blit(self.idle_player_move(image), ((self.width / 2) + self.x, (self.height / 2) + self.y))
            self.player_body = pygame.Rect(((self.width / 2) + self.x, (self.height / 2) + self.y), (32, 56))

            #pygame.draw.rect(screen, (255, 0, 0), Rect(((self.width / 2) + self.x, (self.height / 2) + self.y), (32, 56)), 1) # <-- enable this when testing

        else:
            screen.blit(self.idle_player_move(0), ((self.width / 2) + self.x, (self.height / 2) + self.y))

        return image

    def playerBody(self):
        return self.player_body
