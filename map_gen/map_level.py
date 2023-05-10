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
    
    def lerp_color(self, color1, color2, t):
        return pygame.Color(
        int(color1.r + t * (color2.r - color1.r)),
        int(color1.g + t * (color2.g - color1.g)),
        int(color1.b + t * (color2.b - color1.b)),
    )
        
    def get_range_color(self, value):
        dark_blue = pygame.Color(0, 0, 139)
        red = pygame.Color(255, 0, 0)

        # Normalize the value from [-1, 1] to [0, 1]
        normalized_value = (value + 1) / 2

        # Interpolate between dark blue and red
        return self.lerp_color(dark_blue, red, normalized_value)
    
    def draw_map(self, screen):
        map = self.generate_map() # generate map
        
        x = 0
        y = 0
        
        # drawing
        for col in map:
            for row in col:
                color = self.get_range_color(row)
                #drawing a rect
                pygame.draw.rect(screen, color, (x, y, 1, 1))
                x += 2
            x = 0
            y += 2
