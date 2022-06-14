# this is the first level, this tha basis of eeryhing

import pygame

def lvl1(play_screen, play_run):
    while play_run:
        play_screen.fill((23,23,23))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.update()