import pygame
from pygame.locals import *

# import settings and debug
from resource_path import debug
from settings import *
from screeninfo import get_monitors
import random

# this will be just a generator per level
# this is not the main MAP!
class Map:

    def __init__(self):
        self.map = []

        # screen size
        self.height = get_monitors()[0].height
        self.width = get_monitors()[0].width

        # map size
        colums = random.randint(55, 70)
        rows = random.randint(55, 70)

        for row in range(rows):
            if row == 0:
                self.map.append(['T'] * colums)
            elif row == (rows - 1):
                self.map.append(['B'] * colums)
            else:
                self.map.append([' '] * colums)
                self.map[row][0] = 'L'
                self.map[row][-1] = 'R'

    def upper_chamber(self):
        pass

    def lower_chamber(self):
        pass

    def left_chambers(self):
        pass

    def right_chambers(self):
        pass

    def center_chamber(self): # note that this will determine the number of left, right, upper, and lower chambers
        pass

    def upper_links(self): # NOTE this will detemine the number of center chambers
        pass

    def lower_links(self):
        pass

    def left_links(self):
        pass

    def right_links(self):
        pass
    
    def getMap(self):
        return self.map
