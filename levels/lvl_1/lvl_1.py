# this is the first level, this tha basis of eeryhing
import pygame
from pygame.locals import *
from levels.lvl_1.map import *
from levels.lvl_1.swiches import movement
from map import *
from levels.lvl_1.images_graph import *

def lvl1(play_screen, play_run):

    # movement change

    player_mov = False

    # positioning
    player_init_coords = [0, 0]

    player_x_change = 0
    player_y_change = 0

    # text stuff

    font = pygame.font.Font('freesansbold.ttf', 32)

    # main loop

    while play_run:
        play_screen.fill((23,23,23))

        for event in pygame.event.get():

            # __init__ events

            keys = pygame.key.get_pressed()

            # the events

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # the movements of the character

            change_stat = movement(keys)
            player_x_change = change_stat[0]
            player_y_change = change_stat[1]
            player_mov = change_stat[2]

        # displaying the player

        if player_mov is False:

            player_init_coords = player_init_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)

            stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1, 0, 0)

        else:

            player_init_coords[0] += 0
            player_init_coords[1] += 0

            player_dis(play_screen, player_init_coords[0], player_init_coords[1])

            i = 0
            while i < len(border_blocks_coords):

                border_blocks_coords[i][0] -= player_x_change
                border_blocks_coords[i][1] -= player_y_change

                i += 1

            border_lim(play_screen, border_blocks_coords)
 
        pygame.display.update()
