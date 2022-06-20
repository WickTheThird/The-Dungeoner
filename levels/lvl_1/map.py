# This is the map for LVL1

from levels.lvl_1.images_graph import *

#tile size

TILESIZE_L1 = 64

#the map

WORLD_MAP_L1 = [
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", "P", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
]

# generating the map

def stone_block_dis(screen, WORLD_MAP, TILESIZE):

    dark_stone = dark_stone_wall()

    for row_index, row in enumerate(WORLD_MAP):
           for col_index, col in enumerate(row):
               x = col_index * TILESIZE
               y = row_index * TILESIZE

               if col == 'B':

                  screen.blit(dark_stone, (x, y))
               

def player_update(screen, WORLD_MAP, TILESIZE, change_x, change_y):

    player = main_player()

    for row_index, row in enumerate(WORLD_MAP):
        for col_index, col in enumerate(row):

            x = col_index * TILESIZE + change_x
            y = row_index * TILESIZE + change_y

            if col == 'P':

                screen.blit(player, (x, y))
