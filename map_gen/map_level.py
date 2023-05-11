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
    def __init__(self, width, height, scale=1.0, octaves=15, persistence=0.6, lacunarity=2.5):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.map_data = None

    #? generator
    def generate_map(self):
        map_data = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                nx = x / self.width - 0.5
                ny = y / self.height - 0.5
                value = snoise2(nx * self.scale, ny * self.scale, self.octaves, persistence=self.persistence, lacunarity=self.lacunarity)
                map_data[y][x] = (value + 1) / 2
        return map_data

    #? map color spectrum setter
    def lerp_color(self, color1, color2, t):
        return pygame.Color(
        int(color1.r + t * (color2.r - color1.r)),
        int(color1.g + t * (color2.g - color1.g)),
        int(color1.b + t * (color2.b - color1.b)),
    )

    #? color code map
    def get_range_color(self, value):
        # Define the colors for the different ranges
        dark_blue = pygame.Color(0, 0, 139)
        light_blue = pygame.Color(135, 206, 250)
        green = pygame.Color(34, 139, 34)
        yellow = pygame.Color(255, 215, 0)
        brown = pygame.Color(139, 69, 19)
        white = pygame.Color(255, 255, 255)

        # Define the ranges and corresponding colors
        
        ranges = [
            (-1, dark_blue),
            (-0.5, light_blue),
            (0, green),
            (0.4, yellow),
            (0.7, brown),
            (1, white),
        ]

        # Find the range that the value falls in
        for i in range(len(ranges) - 1):
            if ranges[i][0] <= value < ranges[i+1][0]:
                # Interpolate between the colors for the two ranges
                t = (value - ranges[i][0]) / (ranges[i+1][0] - ranges[i][0])
                return self.lerp_color(ranges[i][1], ranges[i+1][1], t)

        # If the value is outside the ranges, return black
        return pygame.Color(0, 0, 0)

    #? map data
    def get_map_data(self):
        if self.map_data is None:
            self.map_data = self.generate_map()
        return self.map_data

    #? draw map
    
    def draw_map(self, screen, x=0, y=0, chunkSize=16):
        map_data = self.get_map_data()
        for col in map_data:
            current_x = x  # Store the initial x position for each row
            for row in col:
                color = self.get_range_color(row)
                pygame.draw.rect(screen, color, (current_x, y, chunkSize, chunkSize))
                current_x += chunkSize  # Increment the x position without adding a small value
            y += chunkSize
