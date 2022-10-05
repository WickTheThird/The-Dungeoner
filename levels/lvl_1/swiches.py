# These are the on and off swiches for the level

import pygame
from pygame.locals import *
from levels.lvl_1.images_graph import *

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


def map_movement(keys, constant_speed, vertical_speed):

     # The A Key and other related

    if keys[pygame.K_a] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [-1 * constant_speed, 0, 'a']

    elif keys[pygame.K_a] and keys[pygame.K_w]:
        return [-vertical_speed, -vertical_speed, 'aw']

    elif keys[pygame.K_a] and keys[pygame.K_s]:
        return [-vertical_speed, vertical_speed, 'as']

    # The D key and other related
    
    if keys[pygame.K_d] and not (keys[pygame.K_w] or keys[pygame.K_s]):
        return [constant_speed, 0, 'd']
    
    elif keys[pygame.K_d] and keys[pygame.K_w]:
        return [vertical_speed, -vertical_speed, 'dw']

    elif keys[pygame.K_d] and keys[pygame.K_s]:
        return [vertical_speed, vertical_speed, 'ds']

    # Up

    if keys[pygame.K_w] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, -1 * constant_speed, 'w']

    # Down

    if keys[pygame.K_s] and not (keys[pygame.K_a] or keys[pygame.K_d]):
        return [0, constant_speed, 's']

    return [0, 0, 'n']

# note that the enemy movement will be different and thus it will have a different file on its own

# Inventory
