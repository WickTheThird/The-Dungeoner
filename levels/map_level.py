import pygame
from pygame.locals import *

# import settings and debug
from resource_path import debug
from settings import *
from screeninfo import get_monitors
import random

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
            
            if row == 2:
                self.map.append([' '] * colums)
            
            if row == 0:
                self.map.append(['LT'] * colums)
            elif row == (rows - 1):
                self.map.append(['LB'] * colums)
            else:
                self.map.append([' '] * colums)
                self.map[row][0] = 'LL'
                self.map[row][-1] = 'LR'
    
    def mainChamber(self):        
        # PICKING THE CENTER POINT
        xCenter = len(self.map[0]) // 2
        yCenter = len(self.map) // 2
        
        self.map[yCenter][xCenter] = ['MC']
    
    def getMap(self):
        return self.map
