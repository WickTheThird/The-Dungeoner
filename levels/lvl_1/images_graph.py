# these are the images for LEVEL 1

# import modules
import pygame
from pygame.locals import *

# IMAGES

# TILES

#  WALLS #1 (PURPLE) ----------------------

def bottom_left_corner():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/bottom_left_corner_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def bottom_right_corner():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/bottom_right_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def top_left_corner():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/top_left_corner_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def top_right_corner():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/top_right_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))
    
    return tile

def upside_down_wall():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/continous_upsidedown_wall_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def upward_left_wall():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/continous_upward_left_wall_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def upward_right_wall():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/continous_upward_right_wall_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def upward_wall():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/continous_wall_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

# WALLS #2 ----------------------

def bottom_view_light_tile():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/bottom_view_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def top_view_light_tile():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/clean_player_view_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

# THE FLOOR (PURPLE) --------------------------

def clean_purple():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/clean_purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def purple_tile():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/purple_tile.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def dark_stone_wall():

    dark_stone_wall = pygame.image.load("levels/lvl_1/graphics/terrain/stones/dark_stone.webp").convert_alpha()
    dark_stone_wall = pygame.transform.scale(dark_stone_wall, (64, 64))

    return dark_stone_wall

def stone_floor():

    stone_floor = pygame.image.load("levels/lvl_1/graphics/terrain/stones/stone_tile.png").convert_alpha()
    stone_floor = pygame.transform.scale(stone_floor, (64, 64))

    return stone_floor


# DOORS

def left_closed_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/left_closed_door.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def right_closed_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/right_closed_door.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def left_locked_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/left_locked_door.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def right_locked_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/right_locked_door.png').convert_alpha()
    tile  = pygame.transform.scale(tile, (64, 64))

    return tile

def left_open_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/left_open_door.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile

def right_open_door():

    tile = pygame.image.load('levels/lvl_1/graphics/terrain/stones/right_open_door.png').convert_alpha()
    tile = pygame.transform.scale(tile, (64, 64))

    return tile


# TERRAIN (LIQ)

def lava_floor_1():

    lava_floor = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_main.tiff').convert_alpha()
    lava_floor = pygame.transform.scale(lava_floor, (64, 64))

    return lava_floor

def lava_floor_2():

    lava_floor_1 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-1.tiff').convert_alpha()
    lava_floor_2 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-2.tiff').convert_alpha()
    lava_floor_3 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-3.tiff').convert_alpha()
    lava_floor_4 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-4.tiff').convert_alpha()
    lava_floor_5 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-5.tiff').convert_alpha()
    lava_floor_6 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-6.tiff').convert_alpha()
    lava_floor_7 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-7.tiff').convert_alpha()
    lava_floor_8 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-8.tiff').convert_alpha()
    lava_floor_9 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-9.tiff').convert_alpha()
    lava_floor_10 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-10.tiff').convert_alpha()
    lava_floor_11 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-11.tiff').convert_alpha()
    lava_floor_12 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-12.tiff').convert_alpha()
    lava_floor_13 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-13.tiff').convert_alpha()
    lava_floor_14 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-14.tiff').convert_alpha()
    lava_floor_15 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-15.tiff').convert_alpha()
    lava_floor_16 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-16.tiff').convert_alpha()
    lava_floor_17 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-17.tiff').convert_alpha()
    lava_floor_18 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-18.tiff').convert_alpha()
    lava_floor_19 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-19.tiff').convert_alpha()
    lava_floor_20 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-20.tiff').convert_alpha()
    lava_floor_21 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-21.tiff').convert_alpha()
    lava_floor_22 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-22.tiff').convert_alpha()
    lava_floor_23 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-23.tiff').convert_alpha()
    lava_floor_24 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-24.tiff').convert_alpha()
    lava_floor_25 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-25.tiff').convert_alpha()
    lava_floor_26 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-26.tiff').convert_alpha()
    lava_floor_27 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-27.tiff').convert_alpha()
    lava_floor_28 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-28.tiff').convert_alpha()
    lava_floor_29 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-29.tiff').convert_alpha()
    lava_floor_30 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_1/lava-30.tiff').convert_alpha()

    lava_floor_2_sprites = [lava_floor_1, lava_floor_2, lava_floor_3, lava_floor_4, lava_floor_5, lava_floor_6, lava_floor_7, lava_floor_8, lava_floor_9, lava_floor_10,
                            lava_floor_11, lava_floor_12, lava_floor_13, lava_floor_14, lava_floor_15, lava_floor_16, lava_floor_17, lava_floor_18, lava_floor_18, 
                            lava_floor_19, lava_floor_20, lava_floor_21, lava_floor_22, lava_floor_23, lava_floor_24, lava_floor_25, lava_floor_26, lava_floor_27, 
                            lava_floor_28, lava_floor_29, lava_floor_30]

    return lava_floor_2_sprites

def  lava_floor_3():

    lava_floor_1 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-1.tiff').convert_alpha()
    lava_floor_2 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-2.tiff').convert_alpha()
    lava_floor_3 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-3.tiff').convert_alpha()
    lava_floor_4 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-4.tiff').convert_alpha()
    lava_floor_5 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-5.tiff').convert_alpha()
    lava_floor_6 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-6.tiff').convert_alpha()
    lava_floor_7 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-7.tiff').convert_alpha()
    lava_floor_8 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-8.tiff').convert_alpha()
    lava_floor_9 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-9.tiff').convert_alpha()
    lava_floor_10 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-10.tiff').convert_alpha()
    lava_floor_11 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-11.tiff').convert_alpha()
    lava_floor_12 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-12.tiff').convert_alpha()
    lava_floor_13 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-13.tiff').convert_alpha()
    lava_floor_14 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-14.tiff').convert_alpha()
    lava_floor_15 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-15.tiff').convert_alpha()
    lava_floor_16 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-16.tiff').convert_alpha()
    lava_floor_17 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-17.tiff').convert_alpha()
    lava_floor_18 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-18.tiff').convert_alpha()
    lava_floor_19 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-19.tiff').convert_alpha()
    lava_floor_20 = pygame.image.load('levels/lvl_1/graphics/terrain/lava/lava_2/lava-20.tiff').convert_alpha()

    lava_floor_3_sprites = [lava_floor_1, lava_floor_2, lava_floor_3, lava_floor_4, lava_floor_5, lava_floor_6, lava_floor_7, lava_floor_8, lava_floor_9, lava_floor_10,
                            lava_floor_11, lava_floor_12, lava_floor_13, lava_floor_14, lava_floor_15, lava_floor_16, lava_floor_17, lava_floor_18, lava_floor_19, 
                            lava_floor_20]

    return lava_floor_3_sprites

# PLANTS AND STUFF

def tree_1():

    tree = pygame.image.load('levels/lvl_1/graphics/terrain/trees/tree.png').convert_alpha()
    tree = pygame.transform.scale(tree, (64, 32))

    return tree

# CHARACTERS
def main_player():

     player = pygame.image.load('levels/lvl_1/graphics/character/spaceman-1.tiff').convert_alpha()
     player = pygame.transform.scale(player, (64, 64))

     return player

def enemy_0():

    enemy_0 = pygame.image.load('levels/lvl_1/graphics/enemy/0.png').convert_alpha()

    return enemy_0

# ANIMATED CHARACTERS

def player_1_down():

    player_0 = pygame.image.load('levels/lvl_1/graphics/character/player/down/down_0.png').convert_alpha()
    player_1 = pygame.image.load('levels/lvl_1/graphics/character/player/down/down_1.png').convert_alpha()
    player_2 = pygame.image.load('levels/lvl_1/graphics/character/player/down/down_2.png').convert_alpha()
    player_3 = pygame.image.load('levels/lvl_1/graphics/character/player/down/down_3.png').convert_alpha()

    player_sprites = [player_0, player_1, player_2, player_3]

    return player_sprites


def player_1_down_idle():

    down_idle = pygame.image.load('levels/lvl_1/graphics/character/player/down_idle/idle_down.png').convert_alpha()

    return down_idle


def player_1_left():

    player_0 = pygame.image.load('levels/lvl_1/graphics/character/player/left/left_0.png').convert_alpha()
    player_1 = pygame.image.load('levels/lvl_1/graphics/character/player/left/left_1.png').convert_alpha()
    player_2 = pygame.image.load('levels/lvl_1/graphics/character/player/left/left_2.png').convert_alpha()
    player_3 = pygame.image.load('levels/lvl_1/graphics/character/player/left/left_3.png').convert_alpha()

    player_sprites = [player_0, player_1, player_2, player_3]

    return player_sprites


def player_1_left_idle():

    player_idle = pygame.image.load('levels/lvl_1/graphics/character/player/down_idle/idle_down.png').convert_alpha()

    return player_idle


def player_1_right():

    player_0 = pygame.image.load('levels/lvl_1/graphics/character/player/right/right_0.png').convert_alpha()
    player_1 = pygame.image.load('levels/lvl_1/graphics/character/player/right/right_1.png').convert_alpha()
    player_2 = pygame.image.load('levels/lvl_1/graphics/character/player/right/right_2.png').convert_alpha()
    player_3 = pygame.image.load('levels/lvl_1/graphics/character/player/right/right_3.png').convert_alpha()

    player_sprites = [player_0, player_1, player_2, player_3]

    return player_sprites


def player_1_right_idle():

    player_idle = pygame.image.load('levels/lvl_1/graphics/character/player/left_idle/idle_left.png').convert_alpha()

    return player_idle


def player_1_up():

    player_0 = pygame.image.load('levels/lvl_1/graphics/character/player/up/up_0.png').convert_alpha()
    player_1 = pygame.image.load('levels/lvl_1/graphics/character/player/up/up_1.png').convert_alpha()
    player_2 = pygame.image.load('levels/lvl_1/graphics/character/player/up/up_2.png').convert_alpha()
    player_3 = pygame.image.load('levels/lvl_1/graphics/character/player/up/up_3.png').convert_alpha()

    player_sprites = [player_0, player_1, player_2, player_3]

    return player_sprites


def player_1_up_idle():

    player_idle = pygame.image.load('levels/lvl_1/graphics/character/player/up_idle/idle_up.png').convert_alpha()

    return player_idle

# THE INVENTORY

def inventory():

    inventory = pygame.image.load('levels/lvl_1/graphics/dirs/inventory.png').convert_alpha()
    inventory  = pygame.transform.scale(inventory, (1160, 400))

    return inventory

def chest_inventory():

    inventory = pygame.image.load('levels/lvl_1/graphics/dirs/inventory.png').convert_alpha()
    inventory = pygame.transform.scale(inventory, (860, 400))

    return inventory

def inv_slot():

    inv_slot = pygame.image.load('levels/lvl_1/graphics/dirs/inv_slot.png').convert_alpha()
    inv_slot  = pygame.transform.scale(inv_slot, (40, 40))

    return inv_slot

def heart_icon():

    heart_icon = pygame.image.load("levels/lvl_1/graphics/dirs/heart_icon.png").convert_alpha()
    heart_icon = pygame.transform.scale(heart_icon, (32, 32))

    return heart_icon

def sheild_icon():

    sheild_icon = pygame.image.load("levels/lvl_1/graphics/dirs/sheild_icon.png").convert_alpha()
    sheild_icon = pygame.transform.scale(sheild_icon, (40, 40))

    return sheild_icon


# Blocks

# Chests

def wooden_chest():

    global wooden_chest_closed
    wooden_chest_closed = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/chests/wooden_chest/wooden_chest.png").convert_alpha()
    wooden_chest_closed = pygame.transform.scale(wooden_chest_closed, (64, 64))

    global wooden_chest_open
    wooden_chest_open = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/chests/wooden_chest/open_wooden_chest.png").convert_alpha()
    wooden_chest_open = pygame.transform.scale(wooden_chest_open, (64, 64))

    global wooden_chest_sprites
    wooden_chest_sprites = [ wooden_chest_closed, wooden_chest_open]

    return wooden_chest_sprites

def diamond_chest():

    diamond_chest_closed = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/chests/diamond_chest/diamond_chest.png").convert_alpha()
    diamond_chest_closed = pygame.transform.scale(diamond_chest_closed, (64, 64))

    diamond_chest_open = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/chests/diamond_chest/open_diamond_chest.png").convert_alpha()
    diamond_chest_open = pygame.transform.scale(diamond_chest_open, (64, 64))

    diamond_chest_sprites = [ diamond_chest_closed, diamond_chest_open ]

    return diamond_chest_sprites

def chest_inventory():

    inventory = pygame.image.load('levels/lvl_1/graphics/dirs/inventory.png').convert_alpha()
    inventory  = pygame.transform.scale(inventory, (800, 300))

    return inventory


# GEMS

# ENDURI GEMS

def enduri_coin():

    enduri_coin = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/gems/enduri/enduri_coin.png").convert_alpha()
    enduri_coin = pygame.transform.scale(enduri_coin, (32, 32))

    return enduri_coin

# RAHDUL

def rahdul_coin():

    rahdul_coin = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/gems/rahdul/rahdul_coin.png").convert_alpha()
    rahdul_coin = pygame.transform.scale(rahdul_coin, (32, 32))

    return rahdul_coin

# SARDUL

def sardul_coin():

    sardul_coin = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/gems/sardul/sardul_coin.png").convert_alpha()
    sardul_coin = pygame.transform.scale(sardul_coin, (32, 32))

    return sardul_coin

# THRADIL

def thrail_coin():

    sardul_coin = pygame.image.load("levels/lvl_1/graphics/terrain/blocks/gems/thradil/thradil_coin.png").convert_alpha()
    sardul_coin = pygame.transform.scale(sardul_coin, (32, 32))

    return sardul_coin
