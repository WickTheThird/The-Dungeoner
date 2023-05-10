import pygame
from pygame.locals import *

from noise import snoise2

# import settings and debug
from resource_path import debug
from settings import *
from screeninfo import get_monitors
import random

# file imports
from .tiles import *

class Map:
    
    def __init__(self, width, height, scale=1.0, octaves=1, persistence=0.5, lacunarity=2.0):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.map_data = self.generate_map()

    def generate_map(self):
        map_data = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                nx = x / self.width - 0.5
                ny = y / self.height - 0.5
                value = snoise2(nx * self.scale, ny * self.scale, self.octaves, persistence=self.persistence, lacunarity=self.lacunarity)
                map_data[y][x] = (value + 1) / 2  # Rescale from -1.0:+1.0 to 0.0:1.0

        return map_data
