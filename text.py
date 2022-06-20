# here will go implemented text
# positions of the text
# and other styling

import pygame
from pygame.locals import *

from resource_path import resource_path

pygame.init()

# colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0,255,255)
dark_blue = (28, 0, 209)
black = (0,0,0)

# fonts

font = pygame.font.Font('freesansbold.ttf', 32)
font_play = pygame.font.Font('freesansbold.ttf', 100)
font_start_p = pygame.font.Font('freesansbold.ttf', 80)

# text
play = font.render("Start",  False, blue)
about = font.render("About", False, blue)
levels = font.render("Levels", False, blue)
exit = font.render("Quit", False, blue)

# text position
play_x = 0
play_y = 210

about_x = 0
about_y = 310

levels_x = 0
levels_y = 410

exit_x = 0
exit_y = 510

lvl_x = 420
lvl_y = 200

start_p_x = 490
start_p_y = 460

# the play section

lvl_nr = font_play.render("Level 1".format(), False, black)
start_p = font_start_p.render("Start".format(), False, black)
