# these are the images for LEVEL 1

# import modules
import pygame
from pygame.locals import *

# IMAGES

# TILES
def dark_stone_wall():

    dark_stone_wall = pygame.image.load("levels/lvl_1/graphics/terrain/stones/dark_stone.webp").convert_alpha()
    dark_stone_wall = pygame.transform.scale(dark_stone_wall, (64, 64))

    return dark_stone_wall

def stone_floor():

    stone_floor = pygame.image.load("levels/lvl_1/graphics/terrain/stones/stone_tile.png").convert_alpha()
    stone_floor = pygame.transform.scale(stone_floor, (64, 64))

    return stone_floor

def lava_floor_1():

    lava_floor = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_main.tiff').convert_alpha()
    lava_floor = pygame.transform.scale(lava_floor, (64, 64))

    return lava_floor

def lava_floor_2():

    return 

def  lava_floor_3():

    return

# PLANTS AND STUFF

def tree_1():

    tree = pygame.image.load('levels/lvl_1/graphics/terrain/trees/tree.png').convert_alpha()
    tree = pygame.transform.scale(tree, (64, 32))

    return tree

# CHARACTERS
def main_player():

     player = pygame.image.load('levels/lvl_1/graphics/character/spaceman-1.tiff').convert_alpha()
     player = pygame.transform.scale(player, (64, 64))

     return player

def enemy_0():

    enemy_0 = pygame.image.load('levels/lvl_1/graphics/enemy/0.png').convert_alpha()

    return enemy_0
