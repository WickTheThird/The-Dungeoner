# this is the first level, this tha basis of eeryhing

import pygame
from pygame.locals import *
from levels.lvl_1.map import *

# importing from files
from map import *
from images_graph import *

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

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:

                # moving the character

                # going vertically

                # up-right
                if event.key == pygame.K_d and event.key == pygame.K_w:
                    print("UP-RIGHT has been pressed")

                    player_y_change += 0
                    player_x_change += 0

                    player_mov = True
                
                # down-right
                if event.key == pygame.K_d and event.key == pygame.K_s:
                    print("DOWN-RIGHT has been pressed")

                    player_y_change -= 0
                    player_x_change += 0
                
                # up-left
                if event.key == pygame.K_a and event.key == pygame.K_w:
                    print("UP-LEFT has been pressed")

                    player_y_change += 0
                    player_x_change -= 0
                
                # down-left
                if event.key == pygame.K_a and event.key == pygame.K_s:
                    print("DOWN-LEFT has been pressed")

                    player_y_change -= 0
                    player_x_change -= 0

                # right_left (respectively)
                if event.key == pygame.K_d and not (event.key == pygame.K_s or event.key == pygame.K_w):
                    print("D has been pressed -- RIGHT")

                    player_mov = True

                    player_x_change += 10

                if event.key == pygame.K_a and not (event.key == pygame.K_s or event.key == pygame.K_w):
                    print("A has been pressed -- LEFT")
                    
                    player_x_change -= 10

                    player_mov = True

                # down_up (respectively)
                if event.key == pygame.K_s and not (event.key == pygame.K_a or event.key == pygame.K_d):
                    print("S has been pressed --  DOWN")
                   
                    player_y_change += 10

                    player_mov = True

                if event.key == pygame.K_w and not (event.key == pygame.K_a or event.key == pygame.K_d):
                    print("W has been pressed -- UP")
                    
                    player_y_change -= 10

                    player_mov = True


            
            if event.type == pygame.KEYUP:
                
                # stopping the character
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_y_change = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player_x_change = 0

        
        # displaying the borders
        stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)

        # displaying the player

        if player_mov is False:
            player_init_coords = player_init_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)
        else:
            player_init_coords[0] += + player_x_change
            player_init_coords[1] += player_y_change

            player_dis(play_screen, player_init_coords[0], player_init_coords[1])

        pygame.display.update()
