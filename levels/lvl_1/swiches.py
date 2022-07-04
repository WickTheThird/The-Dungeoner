# These are the on and off swiches for the level

import pygame
from pygame.locals import *

def movement(keys):

    # The A Key and other related
    
    if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [-4, 0, True]
    
    elif keys[pygame.K_a] and keys[pygame.K_w]:
        return [-3, -3, True]

    elif keys[pygame.K_a] and keys[pygame.K_s]:
        return [-3, 3, True]

    # The D key and other related
    
    if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [4, 0, True]
    
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        return [3, -3, True]

    elif keys[pygame.K_d] and keys[pygame.K_s]:
        return [3, 3, True]

    # Up

    if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, -4, True]
    
    # Down

    if keys[pygame.K_s]and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, 4, True]
    
    return [0, 0, True]
