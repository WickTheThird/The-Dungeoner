# these are the images for LEVEL 1

# import modules
import pygame
from pygame.locals import *

# IMAGES

# TILES
def dark_stone_wall(): 
    dark_stone_wall = pygame.image.load("levels/lvl_1/graphics/terrain/dark_stone.webp")
    dark_stone_wall = pygame.transform.scale(dark_stone_wall, (64, 64))

    return dark_stone_wall

def stone_floor():
    stone_floor = pygame.image.load("levels/lvl_1/graphics/terrain/stone_tile.png")
    stone_floor = pygame.transform.scale(stone_floor, (64, 64))

    return stone_floor

# CHARACTERS
def main_player():

     player = pygame.image.load('levels/lvl_1/graphics/character/spaceman-1.tiff')
     player = pygame.transform.scale(player, (64, 64))

     return player
