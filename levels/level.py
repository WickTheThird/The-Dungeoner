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
