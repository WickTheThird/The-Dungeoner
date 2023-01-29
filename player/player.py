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

    def idleAnimation(self, image=0):

        file = self.player_idle + str(image) + '.png'

        idle_player = pygame.image.load(file).convert_alpha()
        idle_player = pygame.transform.scale(idle_player, (32, 56))

        return idle_player

    def run(self, screen, state, image=0):
        self.clock.tick(25)
        
        if state is True:
            screen.blit(self.idleAnimation(image), ((self.width / 2), (self.height / 2)))
            self.player_body = pygame.Rect(((self.width / 2), (self.height / 2)), (32, 56))
        else:
            screen.blit(self.idleAnimation(0), ((self.width / 2), (self.height / 2)))

        return [state, image]

    def playerBody(self):
        return Rect(((self.width / 2), (self.height / 2)), (32, 56))
