# library stuff
import pygame
from pygame.locals import *

# files import
from map import *
from text import *
from swiches import *
from images_graph import *
from init_pos import *

pygame.init()

#screen
screen = pygame.display.set_mode((1158, 775))

#title
pygame.display.set_caption("Nomad")
theme = pygame.image.load("wallpaper.jpeg")

#icon
icon = pygame.image.load("treasure-map.png")
pygame.display.set_icon(icon)


#main loop -----------------------------------------------------------------
run = True

# value used in the spaceman animation process
spaceman_value = 0
# --> this will be used as a framerate handler
clock = pygame.time.Clock()

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

        # end of __init__

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if play_button.collidepoint(mouse_pos):
                play = font.render("Start", False, cyan)
                print("The PLAY button has been pushed!")

                # button settings
                over_button = False

                play_dis = False
                about_dis = False
                levels_dis = False
                exit_dis = False

                # title and spaceman
                title_dis = False
                spaceman_dis = False

                # now we must do the block animation
                stone_load = True
                
            elif about_button.collidepoint(mouse_pos):
                about = font.render("About", False, cyan)

                about_stone = True
                back_arrow = True

                print("The About button has been pushed!")
            
            elif level_button.collidepoint(mouse_pos):
                levels = font.render("Levels", False, cyan)

                book_load = True
                back_arrow = True

                print("The Level button has been pushed!")
            
            elif exit_button.collidepoint(mouse_pos):
                exit = font.render("Quit", False, cyan)
                pygame.quit()
                quit()

            if back_dis.collidepoint(mouse_pos) and back_arrow is True and about_stone is True:
                 about_stone = False
            
            elif back_dis.collidepoint(mouse_pos) and back_arrow is True and book_load is True:
                book_load = False
        
        if event.type == pygame.MOUSEBUTTONUP:

           play = font.render("Start",  False, blue)
           about = font.render("About",  False, blue)
           levels = font.render("Levels",  False, blue)
           exit = font.render("Quit",  False, blue)

    # end of the menu section

    # the PLAY section
    # displaying blocks or anyother pieces of graphics 

    if stone_load == False:
        screen.blit(stone_wall, (-1300, 0))
    
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

        if book_load_x >= 00:
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

    pygame.display.update()
