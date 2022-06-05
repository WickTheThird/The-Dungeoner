import pygame, math, sys
from pygame.locals import *
pygame.init()

#screen
screen = pygame.display.set_mode((1000, 800))

#title
pygame.display.set_caption("Nomad")
theme = pygame.image.load("wallpaper.jpeg")

#icon
icon = pygame.image.load("treasure-map.png")
pygame.display.set_icon(icon)

# -------------------------------------------------------------------------
# Notes

# now we need to red 

# --> At the end of styling the sheet <--

# then you must try and make a mouse tracking support for a click funtion
# for now we shall not require a hover effect (but we can study further)

# End of Notes
# -------------------------------------------------------------------------

# colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# fonts
font = pygame.font.Font('freesansbold.ttf', 32)

# text
play = font.render("Start",  False, blue)

about = font.render("About", False, blue)

levels = font.render("Levels", False, blue)

exit = font.render("Quit", False, blue)

# text position
play_x = 0
play_y = 210

about_x = 0
about_y = 310

levels_x = 0
levels_y = 410

exit_x = 0
exit_y = 510

# block timing

play_block = False
about_block = False
level_block = False
exit_block = False

# images and gifs/animations
title = pygame.image.load("nomad.png")

space_man_sprites = [ pygame.image.load("graphics/SpaceMan/spaceman-1.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-2.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-3.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-4.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-5.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-6.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-7.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-8.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-9.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-10.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-11.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-12.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-13.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-14.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-15.tiff"),
    pygame.image.load("graphics/SpaceMan/spaceman-16.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-17.tiff"), pygame.image.load("graphics/SpaceMan/spaceman-18.tiff") ]

#main loop
run = True

# value used in the spaceman animation process
spaceman_value = 0
# --> this will be used as a framerate handler
clock = pygame.time.Clock()

while run:

    #screen styles
    screen.fill((55,198,255))
    screen.blit(theme, (0, 0))

    screen.blit(title, (250, 10))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # the meniu

    # text movements
    play_x += 3.7
    about_x += 3.7
    levels_x += 3.7
    exit_x += 3.7

    # text and box settings
    if play_x >= 455:
        play_x = 455
        play_block = True

    if about_x >= 450:
        about_x = 450
        about_block = True
    
    if levels_x >= 445:
        levels_x = 445
        level_block = True

    if exit_x >= 458:
        exit_x = 458
        exit_block = True

    # displaying the box and placing the texts
    screen.blit(play, (play_x, play_y))
    screen.blit(about, (about_x, about_y))
    screen.blit(levels, (levels_x, levels_y))
    screen.blit(exit, (exit_x, exit_y))

    if play_block is True:
        pygame.draw.rect(screen, blue, pygame.Rect(350, 200, 300, 50), 2)

    if about_block is True:
        pygame.draw.rect(screen, blue, pygame.Rect(350, 300, 300, 50), 2)

    if level_block is True:
        pygame.draw.rect(screen, blue, pygame.Rect(350, 400, 300, 50), 2)
    
    if exit_block is True:
        pygame.draw.rect(screen, blue, pygame.Rect(350, 500, 300, 50), 2)
    

    # adding the spaceman waving animation

    if play_block is True and about_block is True and level_block is True and exit_block is True:
        # setting the framerate
        clock.tick(20)

        if spaceman_value >= len(space_man_sprites):
            spaceman_value = 0

        image = space_man_sprites[spaceman_value]

        screen.blit(image, (470, 600))

        spaceman_value += 1

    # end of the menu section

    pygame.display.update()
