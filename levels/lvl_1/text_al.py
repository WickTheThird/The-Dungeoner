# here will go implemented text
# positions of the text
# and other styling

import pygame
from pygame.locals import *

pygame.init()

# colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0,255,255)
dark_blue = (28, 0, 209)
black = (0,0,0)

dark_green = (0, 17, 0)
swamp_yellow = (99, 86, 65)

# __init__ color

start_color = swamp_yellow
about_color = swamp_yellow
levels_color = swamp_yellow
quit_color = swamp_yellow

# fonts

font = pygame.font.Font('freesansbold.ttf', 32)
font_play = pygame.font.Font('freesansbold.ttf', 100)
font_start_p = pygame.font.Font('freesansbold.ttf', 80)

font_title = pygame.font.Font('freesansbold.ttf', 200)

# text
play = font.render("Start",  False, start_color)
about = font.render("About", False, about_color)
levels = font.render("Levels", False, levels_color)
exit = font.render("Quit", False, quit_color)

# text position
play_x = 210
play_y = 370

about_x = 200
about_y = 440

levels_x = 205
levels_y = 510

exit_x = 215
exit_y = 580

lvl_x = 420
lvl_y = 200

start_p_x = 490
start_p_y = 460

# the play section

lvl_nr = font_play.render("Level 1".format(), False, black)
start_p = font_start_p.render("Start".format(), False, black)
