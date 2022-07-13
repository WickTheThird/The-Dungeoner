# this is the first level, this tha basis of eeryhing
from math import fabs
from pickle import TRUE
from numpy import False_
import pygame
from pygame.locals import *
from levels.lvl_1.map import *
from levels.lvl_1.swiches import map_movement, movement
from map import *
from levels.lvl_1.images_graph import *

def lvl1(play_screen, play_run):

    # movement change

    player_mov = False
    player_state = False

    # positioning
    player_init_coords = [0, 0]

    player_x_change = 0
    player_y_change = 0

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

            # the movements of the blocks

            block_movement = map_movement(keys)
            block_x_change = block_movement[0]
            block_y_change = block_movement[1]

        # displaying the player

        if player_mov is False:

            player_init_coords = player_init_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)

            stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1, 0, 0)

        else:

            i = 0
            while i < len(blocks_coords):

                blocks_coords[i][1] -= block_x_change
                blocks_coords[i][2] -= block_y_change

                blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                i += 1
            
            player_col_dec = pygame.Rect(player_init_coords[0], player_init_coords[1], 64, 64)

            player_state = border_lim(play_screen, blocks_coords, player_col_dec, blocks_col_dec)

            if player_state is True:

                player_init_coords[0] -= block_x_change
                player_init_coords[1] -= block_y_change

                player_dis(play_screen, player_init_coords[0], player_init_coords[1])

            elif player_state is False:

                if player_init_coords[0] > 400 or player_init_coords[0] < 100:
                    player_init_coords[0] += 0

                else:
                    player_init_coords[0] += player_x_change

                if player_init_coords[1] < 100 or player_init_coords[1] > 700:
                    player_init_coords[1] += 0

                else:
                    player_init_coords[1] += player_y_change

                player_dis(play_screen, player_init_coords[0], player_init_coords[1])

        pygame.display.update()
