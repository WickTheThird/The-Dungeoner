# this is the first level, this tha basis of eeryhing

import pygame
from pygame.locals import *
from levels.lvl_1.map import *

# importing from files
from map import *
from images_graph import *

def lvl1(play_screen, play_run):

    # positioning

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

                # right_left (respectively)
                if event.key == pygame.K_d:
                    print("D has been pressed -- RIGHT")

                    player_x_change = 10

                if event.key == pygame.K_a:
                    print("A has been pressed -- LEFT")
                    
                    player_x_change = -10

                # down_up (respectively)
                if event.key == pygame.K_s:
                    print("S has been pressed --  DOWN")
                   
                    player_y_change = 10

                if event.key == pygame.K_w:
                    print("W has been pressed -- UP")
                    
                    player_y_change = -10
            
            if event.type == pygame.KEYUP:
                
                # stopping the character
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_y_change = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player_x_change = 0

        
        stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)
        player_update(play_screen, WORLD_MAP_L1, TILESIZE_L1, player_x_change, player_y_change)
        pygame.display.update()
