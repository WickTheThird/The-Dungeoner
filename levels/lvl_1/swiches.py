# These are the on and off swiches for the level

import pygame
from pygame.locals import *

def movement(keys):

    # The A Key and other related
    
    if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [-10, 0, True]
    
    elif keys[pygame.K_a] and keys[pygame.K_w]:
        return [-9, -9, True]

    elif keys[pygame.K_a] and keys[pygame.K_s]:
        return [-9, 9, True]

    # The D key and other related
    
    if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [10, 0, True]
    
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        return [9, -9, True]

    elif keys[pygame.K_d] and keys[pygame.K_s]:
        return [9, 9, True]

    # Up

    if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, -10, True]

    # Down

    if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, 10, True]
    
    return [0, 0, True]


def map_movement(keys):

     # The A Key and other related
    
    if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [-20, 0]
    
    elif keys[pygame.K_a] and keys[pygame.K_w]:
        return [-19, -19]

    elif keys[pygame.K_a] and keys[pygame.K_s]:
        return [-19, 19]

    # The D key and other related
    
    if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [20, 0]
    
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        return [19, -19]

    elif keys[pygame.K_d] and keys[pygame.K_s]:
        return [19, 19]

    # Up

    if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, -20]

    # Down

    if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, 20]

    return [0, 0]

# note that the enemy movement will be different and thus it will have a different file on its own
