import pygame
from pygame.locals import *

# import settings and debug
from resource_path import debug
from settings import *
from screeninfo import get_monitors
import random

# file imports
from .tiles import *

class Map:

    def __init__(self):
        self.map = []

    def mainChamber(self):        
        pass
    
    def getMap(self):
        return self.map
