#!/usr/bin/env python3
# library stuff

import pygame
from pygame.locals import *

# files import
from map import *
from text import *
from swiches import *
from images_graph import *
from init_pos import *
from levels.lvl_1 import lvl1
from resource_path import resource_path

pygame.init()

#screen
screen = pygame.display.set_mode((1158, 775))
play_screen = pygame.display.set_mode((1158, 775))

#title
pygame.display.set_caption("Nomad")

theme_url = resource_path("wallpaper.jpeg")
theme = pygame.image.load(theme_url)

#icon

icon_url = resource_path("treasure-map.png")
icon = pygame.image.load(icon_url)
pygame.display.set_icon(icon)

#main loop
run = True
play_run = False

spaceman_value = 0
clock = pygame.time.Clock()

# other

# other screen

def lvl_1(play_screen, play_run):
    lvl1(play_screen, play_run)

while run:

    #screen styles
    screen.fill((55,198,255))
    screen.blit(theme, (0, 0))

    if title_dis is True:
        screen.blit(title, (330, 10))

    # the meniu

    # text movements
    play_x += 3.7
    about_x += 3.7
    levels_x += 3.7
    exit_x += 3.7

    # text and box settings
    if play_x >= 505:
        play_x = 532
        play_block = True

    if about_x >= 520:
        about_x = 520
        about_block = True
    
    if levels_x >= 515:
        levels_x = 515
        level_block = True

    if exit_x >= 533:
        exit_x = 533
        exit_block = True

    # displaying the box and placing the texts
    if over_button is True:
        screen.blit(play, (play_x, play_y))
        screen.blit(about, (about_x, about_y))
        screen.blit(levels, (levels_x, levels_y))
        screen.blit(exit, (exit_x, exit_y))

    if play_block is True and play_dis is True:
        play_button = pygame.Rect((350, 200, 300, 50))
        pygame.draw.rect(screen, blue, pygame.Rect(420, 200, 300, 50), 2)

    if about_block is True and about_dis is True:
        about_button = pygame.Rect((350, 300, 300, 50))
        pygame.draw.rect(screen, blue, pygame.Rect(420, 300, 300, 50), 2)

    if level_block is True and levels_dis is True:
        level_button = pygame.Rect((350, 400, 300, 50))
        pygame.draw.rect(screen, blue, pygame.Rect(420, 400, 300, 50), 2)
    
    if exit_block is True and exit_dis is True:
        exit_button = pygame.Rect((350, 500, 300, 50))
        pygame.draw.rect(screen, blue, pygame.Rect(420, 500, 300, 50), 2)


    # adding the spaceman waving animation

    if play_block is True and about_block is True and level_block is True and exit_block is True and spaceman_dis is True:

        # setting the framerate
        clock.tick(20)

        if spaceman_value >= len(space_man_sprites):
            spaceman_value = 0

        image = space_man_sprites[spaceman_value]

        screen.blit(image, (540, 600))

        spaceman_value += 1

    #events
    for event in pygame.event.get():

        # __init__
        back_dis = pygame.draw.circle(screen, (0,0,0), [40, 40], 20, 1)
        start_p_dis = pygame.Rect(420, 450, 350, 100)

        # end of __init__
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            try:
                if play_button.collidepoint(mouse_pos) and play_dis is True:
                    play = font.render("Start", False, cyan)
                    print("The PLAY button has been pushed!")

                    # dissapearing text
                    over_button = False

                    # dissapearing boxes
                    play_dis = False
                    about_dis = False
                    exit_dis = False
                    levels_dis = False

                    title_dis = False
                    spaceman_dis = False

                    # now we must do the block animation
                    stone_load = True

                    #start stuff
                    start_button_p = True

                elif about_button.collidepoint(mouse_pos) and about_dis is True:
                    about = font.render("About", False, cyan)
                    print("The About button has been pushed!")

                    # dissapearing text
                    over_button = False

                    # disapering boxes
                    play_dis = False
                    about_dis = False
                    exit_dis = False
                    levels_dis = False

                    # the main page animations
                    spaceman_dis = False
                    title_dis = False

                    # animation enabled
                    about_stone = True

                    # return button
                    back_arrow = True
                
                elif level_button.collidepoint(mouse_pos) and levels_dis is True:
                    levels = font.render("Levels", False, cyan)
                    print("The Level button has been pushed!")

                    # dissapearing text
                    over_button = False

                    # dissapearing boxes
                    play_dis = False
                    about_dis = False
                    levels_dis = False
                    exit_dis = False

                    # the main page animations
                    spaceman_dis = False
                    title_dis = False

                    # animation enabled ``
                    book_load = True

                    # return button
                    back_arrow = True
                
                elif exit_button.collidepoint(mouse_pos) and exit_dis is True:
                    exit = font.render("Quit", False, cyan)
                    print("The Quit button has been pushed!")

                    # NO EVENTS REQUIRED, BUT EXIT
                    pygame.quit()
                    quit()

                if back_dis.collidepoint(mouse_pos) and back_arrow is True and about_stone is True:

                   # dissapearing animation
                   about_stone = False

                   # reapearing text
                   over_button = True

                   # reapeaaring main animations on the main page
                   title_dis = True
                   spaceman_dis = True

                   # reapearing boxes
                   play_dis = True
                   about_dis = True
                   levels_dis = True
                   exit_dis = True

                   #color
                   about = font.render("About", False, blue)

                
                elif back_dis.collidepoint(mouse_pos) and back_arrow is True and book_load is True:
                    book_load = False

                    # reapearing text
                    over_button = True

                   # reapearing boxes
                    play_dis = True
                    about_dis = True
                    levels_dis = True
                    exit_dis = True

                    # reapeaaring main animations on the main page
                    title_dis = True
                    spaceman_dis = True

                    # text and color/
                    levels = font.render("Levels", False, blue)

                if start_p_dis.collidepoint(mouse_pos) and stone_wall_x >= 0:
                    play_run = True

            except:
                pass

    # end of the menu section

    # the PLAY section
    # displaying blocks or anyother pieces of graphics 

    
    if about_stone == False and back_arrow is False:
        screen.blit(white_stone_wall, (-1300, 0))

    # displaying text and other text related graphics

    if stone_load == True:
        
        stone_wall_x += 10

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

        white_stone_wall_x -= 70

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
        
        book_load_x -= 70

        if book_load_x <= -1200:
            book_load_x = -1200
        
        screen.blit(book_shelf, (book_load_x, 0))
    
    # END OF THE MENU

    # start of PLAY run

    if stone_load is True and stone_wall_x == 0:
        screen.blit(lvl_nr, (lvl_x, lvl_y))
        screen.blit(start_p, (start_p_x, start_p_y))
        pygame.draw.rect(screen, blue, pygame.Rect(420, 450, 350, 100), 2)

        start_button_p = True
    
    if play_run is True:
        lvl_1(play_screen, play_run)

    pygame.display.update()
