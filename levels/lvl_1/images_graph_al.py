# here we shall load images, gifs and other pieces of graphics
# they all shall be initialized here

# modeules
import pygame
from pygame.locals import *

# local resources
from resource_path import resource_path

pygame.init()
screen = pygame.display.set_mode((1158, 775))

# loading the images and animations 

# background main

theme_sprite_1 = pygame.image.load('graphics/background_main/background_main-1 (dragged).tiff').convert_alpha()
theme_sprite_1 = pygame.transform.scale(theme_sprite_1, (1160, 775))

theme_sprite_2 = pygame.image.load('graphics/background_main/background_main-2 (dragged).tiff').convert_alpha()
theme_sprite_2 = pygame.transform.scale(theme_sprite_2, (1160, 775))

theme_sprite_3 = pygame.image.load('graphics/background_main/background_main-3 (dragged).tiff').convert_alpha()
theme_sprite_3 = pygame.transform.scale(theme_sprite_3, (1160, 775))

theme_sprite_4 = pygame.image.load('graphics/background_main/background_main-4 (dragged).tiff').convert_alpha()
theme_sprite_4 = pygame.transform.scale(theme_sprite_4, (1160, 775))

theme_sprite_5 = pygame.image.load('graphics/background_main/background_main-5 (dragged).tiff').convert_alpha()
theme_sprite_5 = pygame.transform.scale(theme_sprite_5, (1160, 775))

theme_sprite_6 = pygame.image.load('graphics/background_main/background_main-6 (dragged).tiff').convert_alpha()
theme_sprite_6 = pygame.transform.scale(theme_sprite_6, (1160, 775))

theme_sprite_7 = pygame.image.load('graphics/background_main/background_main-7 (dragged).tiff').convert_alpha()
theme_sprite_7 = pygame.transform.scale(theme_sprite_7, (1160, 775))

theme_sprite_8 = pygame.image.load('graphics/background_main/background_main-8 (dragged).tiff').convert_alpha()
theme_sprite_8 = pygame.transform.scale(theme_sprite_8, (1160, 775))

theme_sprite_9 = pygame.image.load('graphics/background_main/background_main-9 (dragged).tiff').convert_alpha()
theme_sprite_9 = pygame.transform.scale(theme_sprite_9, (1160, 775))

theme_sprite_10 = pygame.image.load('graphics/background_main/background_main-10 (dragged).tiff').convert_alpha()
theme_sprite_10 = pygame.transform.scale(theme_sprite_10, (1160, 775))

theme_sprite_11 = pygame.image.load('graphics/background_main/background_main-11 (dragged).tiff').convert_alpha()
theme_sprite_11 = pygame.transform.scale(theme_sprite_11, (1160, 775))

theme_sprite_12 = pygame.image.load('graphics/background_main/background_main-12 (dragged).tiff').convert_alpha()
theme_sprite_12 = pygame.transform.scale(theme_sprite_12, (1160, 775))

theme_sprite_13 = pygame.image.load('graphics/background_main/background_main-13 (dragged).tiff').convert_alpha()
theme_sprite_13 = pygame.transform.scale(theme_sprite_13, (1160, 775))

theme_sprite_14 = pygame.image.load('graphics/background_main/background_main-14 (dragged).tiff').convert_alpha()
theme_sprite_14 = pygame.transform.scale(theme_sprite_14, (1160, 775))

theme_sprite_15 = pygame.image.load('graphics/background_main/background_main-15 (dragged).tiff').convert_alpha()
theme_sprite_15 = pygame.transform.scale(theme_sprite_15, (1160, 775))

theme_sprite_16 = pygame.image.load('graphics/background_main/background_main-16 (dragged).tiff').convert_alpha()
theme_sprite_16 = pygame.transform.scale(theme_sprite_16, (1160, 775))

theme_sprite_17 = pygame.image.load('graphics/background_main/background_main-17 (dragged).tiff').convert_alpha()
theme_sprite_17 = pygame.transform.scale(theme_sprite_17, (1160, 775))

theme_sprite_18 = pygame.image.load('graphics/background_main/background_main-18 (dragged).tiff').convert_alpha()
theme_sprite_18 = pygame.transform.scale(theme_sprite_18, (1160, 775))

theme_sprite_19 = pygame.image.load('graphics/background_main/background_main-19 (dragged).tiff').convert_alpha()
theme_sprite_19 = pygame.transform.scale(theme_sprite_19, (1160, 775))

theme_sprite_20 = pygame.image.load('graphics/background_main/background_main-20 (dragged).tiff').convert_alpha()
theme_sprite_20 = pygame.transform.scale(theme_sprite_20, (1160, 775))

theme_sprite_21 = pygame.image.load('graphics/background_main/background_main-21 (dragged).tiff').convert_alpha()
theme_sprite_21 = pygame.transform.scale(theme_sprite_21, (1160, 775))

theme_sprite_22 = pygame.image.load('graphics/background_main/background_main-22 (dragged).tiff').convert_alpha()
theme_sprite_22 = pygame.transform.scale(theme_sprite_22, (1160, 775))

theme_sprite_23 = pygame.image.load('graphics/background_main/background_main-23 (dragged).tiff').convert_alpha()
theme_sprite_23 = pygame.transform.scale(theme_sprite_23, (1160, 775))

theme_sprite_24 = pygame.image.load('graphics/background_main/background_main-24 (dragged).tiff').convert_alpha()
theme_sprite_24 = pygame.transform.scale(theme_sprite_24, (1160, 775))

theme_sprite_25 = pygame.image.load('graphics/background_main/background_main-25 (dragged).tiff').convert_alpha()
theme_sprite_25 = pygame.transform.scale(theme_sprite_25, (1160, 775))

theme_sprite_26 = pygame.image.load('graphics/background_main/background_main-26 (dragged).tiff').convert_alpha()
theme_sprite_26 = pygame.transform.scale(theme_sprite_26, (1160, 775))

theme_sprite_27 = pygame.image.load('graphics/background_main/background_main-27 (dragged).tiff').convert_alpha()
theme_sprite_27 = pygame.transform.scale(theme_sprite_27, (1160, 775))

theme_sprite_28 = pygame.image.load('graphics/background_main/background_main-28 (dragged).tiff').convert_alpha()
theme_sprite_28 = pygame.transform.scale(theme_sprite_28, (1160, 775))

theme_sprite_29 = pygame.image.load('graphics/background_main/background_main-29 (dragged).tiff').convert_alpha()
theme_sprite_29 = pygame.transform.scale(theme_sprite_29, (1160, 775))

theme_sprite_30 = pygame.image.load('graphics/background_main/background_main-30 (dragged).tiff').convert_alpha()
theme_sprite_30 = pygame.transform.scale(theme_sprite_30, (1160, 775))

theme_sprite_31 = pygame.image.load('graphics/background_main/background_main-31 (dragged).tiff').convert_alpha()
theme_sprite_31 = pygame.transform.scale(theme_sprite_31, (1160, 775))

theme_sprite_32 = pygame.image.load('graphics/background_main/background_main-32 (dragged).tiff').convert_alpha()
theme_sprite_32 = pygame.transform.scale(theme_sprite_32, (1160, 775))

theme_sprite_33 = pygame.image.load('graphics/background_main/background_main-33 (dragged).tiff').convert_alpha()
theme_sprite_33 = pygame.transform.scale(theme_sprite_33, (1160, 775))

theme_sprite_34 = pygame.image.load('graphics/background_main/background_main-34 (dragged).tiff').convert_alpha()
theme_sprite_34 = pygame.transform.scale(theme_sprite_34, (1160, 775))

theme_sprite_35 = pygame.image.load('graphics/background_main/background_main-35 (dragged).tiff').convert_alpha()
theme_sprite_35 = pygame.transform.scale(theme_sprite_35, (1160, 775))

theme_sprite_36 = pygame.image.load('graphics/background_main/background_main-36 (dragged).tiff').convert_alpha()
theme_sprite_36 = pygame.transform.scale(theme_sprite_36, (1160, 775))

theme_sprite_37 = pygame.image.load('graphics/background_main/background_main-37 (dragged).tiff').convert_alpha()
theme_sprite_37 = pygame.transform.scale(theme_sprite_37, (1160, 775))

theme_sprite_38 = pygame.image.load('graphics/background_main/background_main-38 (dragged).tiff').convert_alpha()
theme_sprite_38 = pygame.transform.scale(theme_sprite_38, (1160, 775))

theme_sprite_39 = pygame.image.load('graphics/background_main/background_main-39 (dragged).tiff').convert_alpha()
theme_sprite_39 = pygame.transform.scale(theme_sprite_39, (1160, 775))


theme_sprites = [theme_sprite_1, theme_sprite_2, theme_sprite_3, theme_sprite_4, theme_sprite_5, theme_sprite_6, theme_sprite_7, theme_sprite_8, theme_sprite_9, theme_sprite_10, 
theme_sprite_11, theme_sprite_12, theme_sprite_13, theme_sprite_14, theme_sprite_15, theme_sprite_16, theme_sprite_17, theme_sprite_18, theme_sprite_19, theme_sprite_20, theme_sprite_21,
theme_sprite_22, theme_sprite_23, theme_sprite_24, theme_sprite_25, theme_sprite_26, theme_sprite_27, theme_sprite_28, theme_sprite_29, theme_sprite_30, theme_sprite_31, theme_sprite_32,
theme_sprite_33, theme_sprite_34, theme_sprite_35, theme_sprite_36, theme_sprite_37, theme_sprite_38, theme_sprite_39]

# spaceman

#space_man_sprites = [pygame.image.load("graphics/SpaceMan/spaceman-1.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-2.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-3.tiff"),
#    pygame.image.load("graphics/SpaceMan/spaceman-4.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-5.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-6.tiff"),
#    pygame.image.load("graphics/SpaceMan/spaceman-7.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-8.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-9.tiff"),
#    pygame.image.load("graphics/SpaceMan/spaceman-10.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-11.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-12.tiff"),
#    pygame.image.load("graphics/SpaceMan/spaceman-13.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-14.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-15.tiff"),
#    pygame.image.load("graphics/SpaceMan/spaceman-16.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-17.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-18.tiff")]

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

icon_url = resource_path("graphics/icons/icon.webp")
icon = pygame.image.load(icon_url)

stone_wall = pygame.image.load("graphics/terrain/dark_brick_wall.png").convert_alpha()
stone_wall = pygame.transform.scale(stone_wall, (1158, 775))

white_stone_wall = pygame.image.load("graphics/terrain/white_stone_wall.png").convert_alpha()
white_stone_wall = pygame.transform.scale(white_stone_wall, (1158, 775))

back_arrow_dis = pygame.image.load("graphics/dirs/back-button.png").convert_alpha()
back_arrow_dis = pygame.transform.scale(back_arrow_dis, (40, 40))

book_shelf = pygame.image.load("graphics/terrain/book_shelf.png").convert_alpha()
book_shelf = pygame.transform.scale(book_shelf, (1160, 775))

scroll_dir = pygame.image.load('graphics/scroll.png').convert_alpha()
scroll_dir = pygame.transform.scale(scroll_dir, (300, 350))
