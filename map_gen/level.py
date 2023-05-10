import pygame
from pygame.locals import *
from map_gen.map_level import Map
from player.player import Player
from settings import *
from screeninfo import get_monitors

class LevelBase:

    def __init__(self):
        # pygame setup
        pygame.init()
        
        #printing out the map
        my_map = Map(width=100, height=100, scale=10, octaves=4)
