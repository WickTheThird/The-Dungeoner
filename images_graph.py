# here we shall load images, gifs and other pieces of graphics
# they all shall be initialized here

# modeules
import pygame
from pygame.locals import *

# local resources
from resource_path import resource_path

pygame.init()

# loading the images

title_url = resource_path("nomad.png")
title = pygame.image.load(title_url)

# animations

# spaceman

spaceman_1 = resource_path("graphics/SpaceMan/spaceman-1.tiff")
spaceman_2 = resource_path("graphics/SpaceMan/spaceman-2.tiff")
spaceman_3 = resource_path("graphics/SpaceMan/spaceman-3.tiff")
spaceman_4 = resource_path("graphics/SpaceMan/spaceman-4.tiff")
spaceman_5 = resource_path("graphics/SpaceMan/spaceman-5.tiff")
spaceman_6 = resource_path("graphics/SpaceMan/spaceman-6.tiff")
spaceman_7 = resource_path("graphics/SpaceMan/spaceman-7.tiff")
spaceman_8 = resource_path("graphics/SpaceMan/spaceman-8.tiff")
spaceman_9 = resource_path("graphics/SpaceMan/spaceman-9.tiff")
spaceman_10 = resource_path("graphics/SpaceMan/spaceman-10.tiff")
spaceman_11 = resource_path("graphics/SpaceMan/spaceman-11.tiff")
spaceman_12 = resource_path("graphics/SpaceMan/spaceman-12.tiff")
spaceman_13 = resource_path("graphics/SpaceMan/spaceman-13.tiff")
spaceman_14 = resource_path("graphics/SpaceMan/spaceman-14.tiff")
spaceman_15 = resource_path("graphics/SpaceMan/spaceman-15.tiff")
spaceman_16 = resource_path("graphics/SpaceMan/spaceman-16.tiff")
spaceman_17 = resource_path("graphics/SpaceMan/spaceman-17.tiff")
spaceman_18 = resource_path("graphics/SpaceMan/spaceman-18.tiff")

space_man_sprites = [ pygame.image.load(spaceman_1), pygame.image.load(spaceman_2), pygame.image.load(spaceman_3),
    pygame.image.load(spaceman_4), pygame.image.load(spaceman_5), pygame.image.load(spaceman_6),
    pygame.image.load(spaceman_7), pygame.image.load(spaceman_8), pygame.image.load(spaceman_9),
    pygame.image.load(spaceman_10), pygame.image.load(spaceman_11), pygame.image.load(spaceman_12),
    pygame.image.load(spaceman_13), pygame.image.load(spaceman_14), pygame.image.load(spaceman_15),
    pygame.image.load(spaceman_16), pygame.image.load(spaceman_17), pygame.image.load(spaceman_18) ]

# displaying blocks

def stone_block():
    stone_url = resource_path("graphics/terrain/stone-block.png")
    stone = pygame.image.load(stone_url)
    return stone

def dark_stone_block():
    stone_url = resource_path("graphics/terrain/dark_stone.webp")
    stone = pygame.image.load(stone_url)
    return stone

# display images/walls or other pieces of graphics
# enumeerator positions for images

stone_wall_x = -1300
white_stone_wall_x = -1100
book_load_x = -1200

# the images

stone_wall_url = resource_path("graphics/terrain/dark_brick_wall.png")
stone_wall = pygame.image.load(stone_wall_url)
stone_wall = pygame.transform.scale(stone_wall, (1158, 775))

white_stone_wall_url = resource_path("graphics/terrain/white_stone_wall.png")
white_stone_wall = pygame.image.load(white_stone_wall_url)
white_stone_wall = pygame.transform.scale(white_stone_wall, (1158, 775))

back_arrow_dis_url = resource_path("graphics/dirs/back-button.png")
back_arrow_dis = pygame.image.load(back_arrow_dis_url)
back_arrow_dis = pygame.transform.scale(back_arrow_dis, (40, 40))

book_shelf_url = resource_path("graphics/terrain/book_shelf.png")
book_shelf = pygame.image.load(book_shelf_url)
book_shelf = pygame.transform.scale(book_shelf, (1160, 775))
