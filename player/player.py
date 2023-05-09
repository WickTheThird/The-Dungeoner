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
