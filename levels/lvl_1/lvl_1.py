# this is the first level, this tha basis of eeryhing

import pygame
from pygame.locals import *

# from current directory
from levels.lvl_1.map import *
from levels.lvl_1.swiches import map_movement, movement
from levels.lvl_1.images_graph import *

# from parent directory (recreated in current directory)
from levels.lvl_1.images_graph_al import *

# The Main Menu

def algorythm(screen, run):

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


    stone_wall_x = -1300
    white_stone_wall_x = -1100
    book_load_x = -1200

    # the play section

    lvl_nr = font_play.render("Level 1".format(), False, black)
    start_p = font_start_p.render("Start".format(), False, black)

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
    play_run = False

    # __innit__ play screen stuff

    start_level = False
    start_button_p = False

    # Animation Frame Rate

    theme_value = 0
    clock = pygame.time.Clock()

    # other

    while run:

        #screen styles
        screen.fill((0, 41, 41))

        # background
        clock.tick(20)

        if theme_value >= len(theme_sprites):
            theme_value = 0

        image = theme_sprites[theme_value]
        screen.blit(image, (0, 0))
        theme_value += 1

        screen.blit(scroll_dir, (100, 310))

        # title (on screen)
        title_screen = font_title.render('', False, dark_green)

        # the meniu

        # TEXT and BOX
        screen.blit(play, (play_x, play_y))
        screen.blit(about, (about_x, about_y))
        screen.blit(levels, (levels_x, levels_y))
        screen.blit(exit, (exit_x, exit_y))
        screen.blit(title_screen, (150, 20))

        if play_block is True and play_dis is True:
            play_button = pygame.Rect((152, 360, 200, 50))

        if about_block is True and about_dis is True:
            about_button = pygame.Rect((155, 430, 200, 50))

        if level_block is True and levels_dis is True:
            level_button = pygame.Rect((150, 500, 200, 50))
    

        if exit_block is True and exit_dis is True:
            exit_button = pygame.Rect((153, 570, 200, 50))

        #events
        for event in pygame.event.get():

            # __init__
            back_dis = pygame.draw.circle(screen, (0,0,0), [40, 40], 20, 1)
            start_p_dis = pygame.Rect(420, 450, 350, 100)

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

                if play_button.collidepoint(mouse_pos):

                    start_color = dark_green
                    play = font.render("Start",  False, start_color)

                else:

                    start_color = swamp_yellow
                    play = font.render("Start",  False, start_color)
                
                if about_button.collidepoint(mouse_pos):

                    about_color = dark_green
                    about = font.render("Levels",  False, about_color)

                else:

                    about_color = swamp_yellow
                    about = font.render("Levels",  False, about_color)
                
                if level_button.collidepoint(mouse_pos):

                    level_color = dark_green
                    levels = font.render("About",  False, level_color)

                else:

                    level_color = swamp_yellow
                    levels = font.render("About",  False, level_color)
                
                if exit_button.collidepoint(mouse_pos):

                    exit_color = dark_green
                    exit = font.render("Quit",  False, exit_color)

                else:

                    exit_color = swamp_yellow
                    exit = font.render("Quit",  False, exit_color)

            # end of __init__
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # text coloring

            # button poz
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                try:
                    if play_button.collidepoint(mouse_pos):
                        print("The PLAY button has been pushed!")

                        # dissapearing text
                        over_button = False

                        # dissapearing boxes
                        play_dis = False
                        about_dis = False
                        exit_dis = False
                        levels_dis = False

                        # now we must do the block animation
                        stone_load = True

                        #start stuff
                        play_run = True
                        run = False

                    elif about_button.collidepoint(mouse_pos):
                        print("The About button has been pushed!")

                        # dissapearing text
                        over_button = False

                        # disapering boxes
                        play_dis = False
                        about_dis = False
                        exit_dis = False
                        levels_dis = False

                        # animation enabled
                        about_stone = True

                        # return button
                        back_arrow = True
                    
                    elif level_button.collidepoint(mouse_pos):
                        print("The Level button has been pushed!")

                        # dissapearing text
                        over_button = False

                        # dissapearing boxes
                        play_dis = False
                        about_dis = False
                        levels_dis = False
                        exit_dis = False

                        # animation enabled ``
                        book_load = True

                        # return button
                        back_arrow = True
                    
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        quit()

                    if back_dis.collidepoint(mouse_pos) and back_arrow is True and about_stone is True:

                        # dissapearing animation
                        about_stone = False

                        # reapearing text
                        over_button = True

                        # reapearing boxes
                        play_dis = True
                        about_dis = True
                        levels_dis = True
                        exit_dis = True

                    
                    elif back_dis.collidepoint(mouse_pos) and back_arrow is True and book_load is True:
                        book_load = False

                        # reapearing text
                        over_button = True

                    # reapearing boxes
                        play_dis = True
                        about_dis = True
                        levels_dis = True
                        exit_dis = True

                    if start_p_dis.collidepoint(mouse_pos) and stone_wall_x >= 0:
                        play_run = True
                except:
                    pass

        # end of the menu section

        # the PLAY section
        if about_stone == False and back_arrow is False:
            screen.blit(white_stone_wall, (-1300, 0))

        # displaying text and other text related graphics
        if stone_load == True:
            
            stone_wall_x += 50

            if stone_wall_x >= 0:
                stone_wall_x = 0

            screen.blit(stone_wall, (stone_wall_x, 0))

        # the ABOUT section
        if about_stone == True:
            white_stone_wall_x += 70

            if white_stone_wall_x >= 0:
                white_stone_wall_x = 0

            screen.blit(white_stone_wall, (white_stone_wall_x, 0))

            if back_arrow is True and white_stone_wall_x == 0:
                pygame.draw.circle(screen, (0,0,0), [40, 40], 20, 1)
                screen.blit(back_arrow_dis, (20, 20))

        elif about_stone is False and back_arrow is True:

            white_stone_wall_x -= 100

            if white_stone_wall_x <= -1300:
                white_stone_wall_x = -1300

            screen.blit(white_stone_wall, (white_stone_wall_x, 0))


        # the LEVEL section
        if book_load is True:
            book_load_x += 70

            if book_load_x >= 0:
                book_load_x = 0

            screen.blit(book_shelf, (book_load_x, 0))

            if back_arrow is True and book_load_x == 0:
                pygame.draw.circle(screen, (0,0,0), [40, 40], 20, 1)
                screen.blit(back_arrow_dis, (20, 20))

        elif book_load is False and back_arrow is True:

            book_load_x -= 100

            if book_load_x <= -1200:
                book_load_x = -1200

            screen.blit(book_shelf, (book_load_x, 0))

        # END OF THE MENU
        # start of PLAY rund
        if play_run is True:
            lvl1(screen, play_run)

        pygame.display.update()




# -------------------------------------------- main game/level -----------------------------------------------------------------------




def lvl1(play_screen, play_run):

    # movement change

    player_mov = False

    # Inv state

    inv_state = False

    # positioning

    player_init_coords = [0, 0]

    # colors and other text things

    blue = (0, 0, 255)
    red = (255, 0, 0)

    font = pygame.font.Font('freesansbold.ttf', 32)

    # technical stuff

    character_stats = False

    hp = '100'
    sh = '100'

    # Map Movement influence

    lava_dm_state = False
    moving_map = True

    block_x_change = 0
    block_y_change = 0

    movment_history = ['n']
    idle_state = movment_history[-1]

    character_ind_up = 0
    character_ind_down = 0
    character_ind_left = 0
    character_ind_right = 0

    character_walking_ind = 0

    # frame

    clock = pygame.time.Clock()

    # main loop

    while play_run:
        play_screen.fill((23,23,23))

        # displaying text

        if character_stats is False:
            hearts = font.render(f'Hearts: {hp}', False, blue)
            sheild = font.render(f'Sheild: {sh}', False, blue)

        yes = font.render('Yes', False, blue)
        no = font.render('No', False, red)
        respawn_q = font.render('Respawn:', False, blue)

        # Boxes

        yes_b = pygame.Rect(1000, 30, 128, 32)
        no_b = pygame.Rect(800, 30, 128, 32)

        for event in pygame.event.get():

            # __init__ events

            keys = pygame.key.get_pressed()

            # the events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # the movements of the character

            change_stat = movement(keys)
            player_mov = change_stat[2]

            # characrer inventory

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and inv_state == False:
                    inv_state = True
                elif event.key == pygame.K_e and inv_state == True:
                    inv_state = False

            # the movements of the blocks

            if moving_map is True:

                block_movement = map_movement(keys)
                block_x_change = block_movement[0]
                block_y_change = block_movement[1]
                last = block_movement[2]

                if last == 'a':
                    movment_history.append('a')

                    idle_state = movment_history[-1]

                    character_ind_left += 1

                    if character_ind_left == 4:
                        character_ind_left = 0

                    character_walking_ind = character_ind_left

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_right = 0

                elif last == 'aw':
                    movment_history.append('aw')

                    idle_state = movment_history[-1]

                    character_ind_left += 1

                    if character_ind_left == 4:
                        character_ind_left = 0

                    character_walking_ind = character_ind_left

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_right = 0

                elif last == 'as':
                    movment_history.append('as')

                    idle_state = movment_history[-1]

                    character_ind_left += 1

                    if character_ind_left == 4:
                        character_ind_left = 0

                    character_walking_ind = character_ind_left

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_right = 0

                elif last == 'd':
                    movment_history.append('d')

                    idle_state = movment_history[-1]

                    character_ind_right += 1

                    if character_ind_right == 4:
                        character_ind_right = 0

                    character_walking_ind = character_ind_right

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_left = 0

                elif last == 'dw':
                    movment_history.append('dw')

                    idle_state = movment_history[-1]

                    character_ind_right += 1

                    if character_ind_right == 4:
                        character_ind_right = 0

                    character_walking_ind = character_ind_right

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_left = 0

                elif last == 'ds':
                    movment_history.append('ds')

                    idle_state = movment_history[-1]

                    character_ind_right += 1

                    if character_ind_right == 4:
                        character_ind_right = 0

                    character_walking_ind = character_ind_right

                    character_ind_up = 0
                    character_ind_down = 0
                    character_ind_left = 0

                elif last == 'w':
                    movment_history.append('w')

                    idle_state = movment_history[-1]

                    character_ind_up += 1

                    if character_ind_up == 4:
                        character_ind_up = 0

                    character_walking_ind = character_ind_up

                    character_ind_down = 0
                    character_ind_left = 0
                    character_ind_right = 0
                
                elif last == 's':
                    movment_history.append('s')

                    idle_state = movment_history[-1]

                    character_ind_down += 1

                    if character_ind_down == 4:
                        character_ind_down = 0

                    character_walking_ind = character_ind_down

                    character_ind_up = 0
                    character_ind_left = 0
                    character_ind_right = 0

                elif last == 'n':
                    print('n')
                    idle_state = movment_history[-1]

            else:

                block_x_change = 0
                block_y_change = 0

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_pos = event.pos

                    if yes_b.collidepoint(mouse_pos):

                        moving_map = True
                        sh = '0'
                        hp = '50'
    
                    if no_b.collidepoint(mouse_pos):
                        algorythm(play_screen, True)


        # displaying the player

        if player_mov is False:

            player_init_coords = player_init_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1)
            stone_block_dis(play_screen, WORLD_MAP_L1, TILESIZE_L1, 0, 0)

        else:

            player_border_col = pygame.Rect(player_init_coords[0], player_init_coords[1], 64, 64)

            lava_dm_state = lava_dm(blocks_coords, player_border_col, blocks_col_dec)
            #print(lava_dm_state)

            if lava_dm_state is True:
                i = 0
                while i < len(blocks_coords):

                    blocks_coords[i][1] -= (block_x_change // 3)
                    blocks_coords[i][2] -= (block_y_change // 3)

                    blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                    i += 1
            
            else:

                i = 0
                while i < len(blocks_coords):

                    blocks_coords[i][1] -= (block_x_change)
                    blocks_coords[i][2] -= (block_y_change)

                    blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                    i += 1

            state = border_lim(blocks_coords, player_border_col, blocks_col_dec)

            if state is False:

                map_around_floor(play_screen, blocks_coords)
                player_dis(play_screen, player_init_coords[0], player_init_coords[1], idle_state, character_walking_ind)
                map_around(play_screen, blocks_coords)

            elif state is True:

                if lava_dm_state is True:
                    i = 0
                    while i < len(blocks_coords):

                        blocks_coords[i][1] += (block_x_change // 3)
                        blocks_coords[i][2] += (block_y_change // 3)

                        blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                        i += 1
                else:
                    i = 0
                    while i < len(blocks_coords):

                        blocks_coords[i][1] += (block_x_change)
                        blocks_coords[i][2] += (block_y_change)

                        blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                        i += 1

                map_around_floor(play_screen, blocks_coords)
                player_dis(play_screen, player_init_coords[0], player_init_coords[1], idle_state, character_walking_ind)
                map_around(play_screen, blocks_coords)

        
        # RESPAWN
        
        if lava_dm_state is True:

            new_hp = int(hp) - 1

            hp = str(new_hp)

            if int(hp) <= 0:

                lava_dm_state = False
                moving_map = False

                i = 0
                while i < len(blocks_coords):

                    blocks_coords[i][1] = respawn_point[i][1]
                    blocks_coords[i][2] = respawn_point[i][2]

                    blocks_col_dec[i] = pygame.Rect(blocks_coords[i][1], blocks_coords[i][2], 64, 64)

                    i += 1

                hp = '0'

        # Dispplaying settings

        if character_stats is False:
            play_screen.blit(hearts, (20, 20))
            play_screen.blit(sheild, (20, 60))

        if moving_map is False:

            play_screen.blit(respawn_q, (600, 30))

            pygame.draw.rect(play_screen, blue, pygame.Rect(1000, 30, 128, 32), 1)
            play_screen.blit(yes, (1040, 30))

            pygame.draw.rect(play_screen, red, pygame.Rect(800, 30, 128, 32), 1)
            play_screen.blit(no, (845, 30))
        
        # Inventory
        if inv_state is True:
            play_screen.blit(inventory(), (0, 460))

            #player 
            play_screen.blit(player_1_down_idle(), (854.5, 628))

            # Armor inventory
            play_screen.blit(inv_slot(), (805, 580))
            play_screen.blit(inv_slot(), (865, 580))
            play_screen.blit(inv_slot(), (925, 580))
            play_screen.blit(inv_slot(), (805, 640))
            play_screen.blit(inv_slot(), (805, 700))
            play_screen.blit(inv_slot(), (865, 700))
            play_screen.blit(inv_slot(), (925, 700))
            play_screen.blit(inv_slot(), (925, 640))

            # inventory slots

            diff = 40
            slot_x = 280
            slot_y = 520
            for x in range(50):

                i = x
                if i % 10 == 0:
                    slot_x = 280
                    slot_y += diff

                slot_x += diff

                # draw inventory slots
                play_screen.blit(inv_slot(), (slot_x, slot_y))
            
            # Character stats
            character_stats = True

            if int(hp) < 100:

                # HP RECTANGLE if inv is open and damage take
                dis_hp = 100 - int(hp)
                pygame.draw.rect(play_screen, red, pygame.Rect(170, 561, 20, 100 - dis_hp))
                pygame.draw.rect(play_screen, red, pygame.Rect(170, 561, 20, 100), 1)

                # Sheild Rectangle if inv is open and damage taken
                disp_sheild = 100 - int(sh)
                pygame.draw.rect(play_screen, blue, pygame.Rect(230, 561, 20, 100 - disp_sheild))
                pygame.draw.rect(play_screen, blue, pygame.Rect(230, 561, 20, 100), 1)

            else:
                # HP RECTANGLE if inv is open and no damage is taken
                pygame.draw.rect(play_screen, red, pygame.Rect(170, 561, 20, 100))

                # Sheild Rectangle if inv is open and no damage taken
                pygame.draw.rect(play_screen, blue, pygame.Rect(230, 561, 20, 100))
        else:
            character_stats = False

        pygame.display.update()
