# here will be the on and off swiches
# of any event
# i believe this is necessary as it is hard to keep track of everything on one single large file
# mostly displaying events will go here

import pygame
from pygame.locals import *

pygame.init()

# block timing

play_block = True
about_block = True
level_block = True
exit_block = True

# display status --> Boxes/Shapes

# menu buttons
over_button = True

play_dis = True
about_dis = True
levels_dis = True
exit_dis = True

# menu graphics
spaceman_dis = True
title_dis = True

#section graphics
stone_load = False
about_stone = False
book_load = False

# dir stuff
back_arrow = False

# __innit__ play screen stuff

start_level = False
start_button_p = False

