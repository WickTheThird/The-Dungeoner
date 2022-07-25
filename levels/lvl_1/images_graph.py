# these are the images for LEVEL 1

# import modules
import pygame
from pygame.locals import *

# IMAGES

# TILES
def dark_stone_wall(): 
    dark_stone_wall = pygame.image.load("levels/lvl_1/graphics/terrain/dark_stone.webp").convert_alpha()
    dark_stone_wall = pygame.transform.scale(dark_stone_wall, (64, 64))

    return dark_stone_wall

def stone_floor():
    stone_floor = pygame.image.load("levels/lvl_1/graphics/terrain/stone_tile.png").convert_alpha()
    stone_floor = pygame.transform.scale(stone_floor, (64, 64))

    return stone_floor

# CHARACTERS
def main_player():

     player = pygame.image.load('levels/lvl_1/graphics/character/spaceman-1.tiff').convert_alpha()
     player = pygame.transform.scale(player, (64, 64))

     return player

def tree_1():

    tree = pygame.image.load('levels/lvl_1/graphics/terrain/tree.png').convert_alpha()
    tree = pygame.transform.scale(tree, (256, 256))

    return tree
