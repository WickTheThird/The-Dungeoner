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

            # __init__ events

            keys = pygame.key.get_pressed()

            # the events

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:

                # moving the character

                # right_left (respectively)

                # ---------------------------RIGHT--------------------------------- #
                if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
                    print("D has been pressed -- RIGHT")

                    player_mov = True
                    player_x_change += 3

                elif keys[pygame.K_d] and keys[pygame.K_w]:
                    print("The D and W keys have been peressed -- Moving Right-Up")
                    
                    player_mov = True
                    player_x_change += 1
                    player_y_change -= 1

                elif keys[pygame.K_d] and keys[pygame.K_s]:
                    print("The D and S kays have been pressed -- Moving Right-Down")

                    player_mov = True
                    player_x_change += 1
                    player_y_change += 1

                # ---------------------------LEFT--------------------------------- #

                if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
                    print("A has been pressed -- LEFT")
                    
                    player_mov = True
                    player_x_change -= 3
                    

                elif keys[pygame.K_a] and keys[pygame.K_w]:
                    print("The A and W keys have been pressed --  Moving Left-Up")

                    player_mov = True
                    player_x_change -= 1
                    player_y_change -= 1
                
                elif keys[pygame.K_a] and keys[pygame.K_s]:
                    print("The A and S keys have been pressed --  Moving Left-Down")

                    player_mov = True
                    player_x_change -= 1
                    player_y_change += 1

                # down_up (respectively)

                # ---------------------------DOWN--------------------------------- #
                if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
                    print("S has been pressed --  DOWN")
                   
                    player_mov = True
                    player_y_change += 3

                elif keys[pygame.K_s] and keys[pygame.K_d]:
                    print("S and D have been pressed --  DOWN-RIGHT")

                    player_mov = True
                    player_x_change += 1
                    player_y_change += 1
                
                elif keys[pygame.K_s] and keys[pygame.K_d]:
                    print("S and A have been pressed --  DOWN-LEFT")

                    player_mov = True
                    player_x_change += 1
                    player_y_change += 1

                # ---------------------------UP--------------------------------- #
                if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
                    print("W has been pressed -- UP")
                    
                    player_mov = True
                    player_y_change -= 3

                elif keys[pygame.K_w] and keys[pygame.K_d]:
                    print("S and D have been pressed -- UP-RIGHT")

                    player_mov = True
                    player_x_change += 1
                    player_y_change -= 1

                elif keys[pygame.K_w] and keys[pygame.K_a]:
                    print("S and A have been pressed -- UP-LEFT")

                    player_mov = True
                    player_x_change -= 1
                    player_y_change -= 1
            
            if event.type == pygame.KEYUP:

                # __init__ values

                keys = pygame.key.get_pressed()

                # other events
                
                # stopping the character
                if event.key == pygame.K_w or event.key == pygame.K_s:

                    player_y_change = 0
                    
                    if keys[pygame.K_a] and not keys[pygame.K_w]:
                        print("CHANGE")
                        player_x_change -= 3
                    
                    if keys[pygame.K_d] and not keys[pygame.K_s]:
                        print("CHANGE")
                        player_x_change += 3

                if event.key == pygame.K_a or event.key == pygame.K_d:

                    player_x_change = 0

                    if keys[pygame.K_w] and not keys[pygame.K_a]:
                        print("CHANGE")
                        player_y_change -= 3
                    
                    if keys[pygame.K_s] and not keys[pygame.K_d]:
                        print("CHANGE")

                        player_y_change += 3

        
        # displaying the borders
        stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)

        # displaying the player

        if player_mov is False:
            player_init_coords = player_init_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)
        else:
            player_init_coords[0] += + player_x_change
            player_init_coords[1] += player_y_change

            for x in border_poz:
                if x == player_init_coords:
                    print("BORDER!!!")

            player_dis(play_screen, player_init_coords[0], player_init_coords[1])

        pygame.display.update()
