import pygame, math, sys
pygame.init()

#screen
screen = pygame.display.set_mode((1000, 800))

background = pygame.image.load('clouds.png')

# -------------------------------------------------------------------------
# Notes

# You now must add a Title, with a font
# try and animate something running and then add it at the bottom
# then you must try and make a mouse tracking support for a click funtion
# for now we shall not require a hover effect

# End of Notes
# -------------------------------------------------------------------------

# colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# fonts
font = pygame.font.Font('freesansbold.ttf', 32)

# text
play = font.render("Start",  False, red)

about = font.render("About", False, red)

levels = font.render("Levels", False, red)

exit = font.render("Quit", False, red)

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

#main loop
run = True

while run:

    #screen styles
    screen.fill((55,198,255))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # the meniu

    # text movements
    play_x += 3
    about_x += 3
    levels_x += 3
    exit_x += 3

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

    # end of the menu section

    pygame.display.update()
