# This is the map for LVL1
from levels.lvl_1.images_graph import *

#tile size

TILESIZE_L1 = 64

#the map

WORLD_MAP_L1 = [
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "P", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "T", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "B", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "B", "B", "B", "F", "F", "F", "F", "F", "F", "F", "B", "B", "B", "B", "B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "B", "B", "B", "B", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "B", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "B", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "B", "B", "B", "B", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "F", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "B", "B", "F", "F", "B", "B", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B", "F", "F", "F", "B", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
]

# colours

blue = (0, 0, 255)

# generating the map -------------------------------------

blocks_coords = []
blocks_col_dec = []

black = (0,0,0)

def stone_block_dis(screen, WORLD_MAP, TILESIZE, change_x, change_y):

    dark_stone = dark_stone_wall()
    stone_floor_tile = stone_floor()
    oak_tree = tree_1()

    for row_index, row in enumerate(WORLD_MAP):
           for col_index, col in enumerate(row):
               x = (col_index * TILESIZE) + change_x
               y = (row_index * TILESIZE) + change_y

               blocks_col_dec.append(pygame.Rect(x, y, 64, 64))

               if col == 'B':
                  blocks_coords.append(['B', x, y])

                  screen.blit(dark_stone, (x, y))

               if col == 'F' or col == 'P':
                   blocks_coords.append(['F', x, y])

                   screen.blit(stone_floor_tile, (x, y))

               if col == 'T':
                   blocks_coords.append(['T', x, y])

                   screen.blit(stone_floor_tile, (x, y))
                   screen.blit(oak_tree, (x, y))

# --- this is used to catch the initial coords of the player ---
def player_init_dis(screen, WORLD_MAP, TILESIZE):

    player = main_player()

    for row_index, row in enumerate(WORLD_MAP):
           for col_index, col in enumerate(row):
               x = col_index * TILESIZE + 38
               y = row_index * TILESIZE + 38

               if col == 'P':
                  screen.blit(player, (x, y))

                  return [x, y]

# player ----------------------------------------------

def player_dis(screen, x, y):
    player = main_player()

    screen.blit(player, (x, y))

# blocks ----------------------------------------------

def border_lim(poz, player_poz, block_poz):

    state = False

    for i, x in enumerate(poz):
        collide = pygame.Rect.colliderect(player_poz, block_poz[i])

        if collide and (x[0] == 'B'):
            state  = True

    return state

def map_around(screen, poz):

    dark_stone = dark_stone_wall()
    stone_floor_tile = stone_floor()
    oak_tree = tree_1()

    for x in poz:

        if x[0] == 'B':
            screen.blit(dark_stone, (x[1], x[2]))

        elif x[0] == 'T':

            screen.blit(stone_floor_tile, (x[1], x[2]))
            screen.blit(oak_tree, (x[1], x[2]))

def map_around_floor(screen, poz):

    stone_floor_tile = stone_floor()

    for x in poz:

        if x[0] == 'F':
            screen.blit(stone_floor_tile, (x[1], x[2]))
