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

# fonts
font = pygame.font.Font('freesansbold.ttf', 32)

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

