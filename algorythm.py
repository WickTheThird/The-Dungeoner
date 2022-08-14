# stuff
import pygame
from pygame.locals import *

# files import
from text import *
from swiches import *
from images_graph import *
from levels.lvl_1.lvl_1 import lvl1

pygame.init()

#screen
screen = pygame.display.set_mode((1158, 775))
play_screen = pygame.display.set_mode((1158, 775))

#title
pygame.display.set_caption("---")

#icon
pygame.display.set_icon(icon)

#main loop
run = True
play_run = False

theme_value = 0
clock = pygame.time.Clock()

# other

# other screen
def lvl_1(play_screen, play_run):
    lvl1(play_screen, play_run)

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
        lvl_1(play_screen, play_run)

    pygame.display.update()

# Notes

# The level's section needs redesign...But we can only do it on a tablet...we shall rquire a map (that I have in mind) -- multiple of these --
#                        in order to compensate for each level...foe now if we just do a schech would be fine
# In the About section, we need to add 2 things -- controls -- story ark/a log of the beasts you have met up until now (that would be cool)
#
