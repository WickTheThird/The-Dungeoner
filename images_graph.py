# here we shall load images, gifs and other pieces of graphics
# they all shall be initialized here

# modeules
import pygame
from pygame.locals import *

# local resources
from resource_path import resource_path

pygame.init()
screen = pygame.display.set_mode((1158, 775))

# loading the images

title_url = resource_path("nomad.png")
title = pygame.image.load(title_url).convert_alpha()

# animations

# spaceman

space_man_sprites = [pygame.image.load("graphics/SpaceMan/spaceman-1.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-2.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-3.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-4.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-5.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-6.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-7.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-8.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-9.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-10.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-11.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-12.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-13.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-14.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-15.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-16.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-17.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-18.tiff")]

# displaying blocks

def stone_block():
    stone = pygame.image.load("graphics/terrain/stone-block.png").convert_alpha()
    return stone

def dark_stone_block():
    stone = pygame.image.load("graphics/terrain/dark_stone.webp").convert_alpha()
    return stone

# display images/walls or other pieces of graphics
# enumeerator positions for images

stone_wall_x = -1300
white_stone_wall_x = -1100
book_load_x = -1200

# the images

stone_wall = pygame.image.load("graphics/terrain/dark_brick_wall.png").convert_alpha()
stone_wall = pygame.transform.scale(stone_wall, (1158, 775))

white_stone_wall = pygame.image.load("graphics/terrain/white_stone_wall.png").convert_alpha()
white_stone_wall = pygame.transform.scale(white_stone_wall, (1158, 775))

back_arrow_dis = pygame.image.load("graphics/dirs/back-button.png").convert_alpha()
back_arrow_dis = pygame.transform.scale(back_arrow_dis, (40, 40))

book_shelf = pygame.image.load("graphics/terrain/book_shelf.png").convert_alpha()
book_shelf = pygame.transform.scale(book_shelf, (1160, 775))
