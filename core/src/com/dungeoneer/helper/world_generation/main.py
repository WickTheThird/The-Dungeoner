from perlin_noise import PerlinNoise
import sys
import os
import secrets


class World():

    #! size_x and size_y are the numnber of tiles in the world in the x and y axes respectively
    def __init__(self, size_x, size_y, world_name="New World"):

        self.path = "../../objects/worlds/"
        self.world_name = world_name
        random_seed = self.generate_map_seed()

        self.create_world_dir()
        self.generate_noise_map(size_x, size_y, random_seed)
        self.create_noise_map_file()

        flat_list = [item for noise_list in self.noise_map for item in noise_list]
        self.min_val = min(flat_list)
        self.max_val = max(flat_list)

        self.tile_map = self.create_tile_map([5, 5, 30, 5, 70, 5, 5]) # those weights generates islands
        self.create_tile_map_file()


    def generate_noise_map(self, size_x, size_y, random_seed):

        self.noise_map = []

        noise1 = PerlinNoise(octaves = 3, seed=random_seed)
        noise2 = PerlinNoise(octaves = 6, seed=random_seed)
        noise3 = PerlinNoise(octaves = 12, seed=random_seed)
        noise4 = PerlinNoise(octaves = 24, seed=random_seed)

        xpix, ypix = size_x + 1, size_y + 1
        for j in range(ypix):
            row = []
            for i in range(xpix):
                noise_val = noise1([i/xpix, j/ypix])
                noise_val += 0.5 * noise2([i/xpix, j/ypix])
                noise_val += 0.25 * noise3([i/xpix, j/ypix])
                noise_val += 0.125 * noise4([i/xpix, j/ypix])
                row.append(noise_val)

            self.noise_map.append(row)


    def generate_map_seed(self):
        return int(''.join(secrets.choice("0123456789") for _ in range(16)))


    def create_world_dir(self):

        try:
            self.path += self.world_name + '/'
            os.mkdir(self.path)

        except Exception:
            entries = os.listdir(self.path)
            no_entries = 0

            for file in entries:
                if file == self.world_name:
                    no_entries += 1

            self.world_name += str(no_entries)
            self.path += self.world_name + '/'

            os.mkdir(self.path)


    def create_noise_map_file(self):
        noise_map = self.get_noise_map()
        with open(self.path + "noise_map.txt", 'w') as file:
            for row in noise_map:
                file.write(' '.join(map(lambda x : str(x), row)) + '\n')


    def create_tile_map(self, weights):

        # Terrain Types --> TODO You will have to add more to this as we go
        OCEAN = 0
        OCEAN2 = 1
        OCEAN3 = 2
        BEACH = 3
        GRASS = 4
        MOUNTAIN = 5
        SNOW = 6

        ALL_TERRAIN_TYPES = [OCEAN, OCEAN2, OCEAN3, BEACH, GRASS, MOUNTAIN, SNOW]

        # CALUCLATOR
        total_weights = sum(weights)
        total_range = self.max_val - self.min_val

        # MAX height for each teren type
        max_terrain_heights = []
        previous_height = self.min_val
        for terrain_type in ALL_TERRAIN_TYPES:
            height = total_range * (weights[terrain_type] / total_weights) + previous_height
            max_terrain_heights.append(height)
            previous_height = height
        max_terrain_heights[SNOW] = self.max_val

        map_int = []

        for row in self.get_noise_map():
            map_row = []
            for value in row:
                for terrain_type in ALL_TERRAIN_TYPES:
                    if value <= max_terrain_heights[terrain_type]:
                        map_row.append(terrain_type)
                        break
            map_int.append(map_row)

        return map_int
    
    def create_tile_map_file(self):
        tiled_map = self.get_tiled_map()
        mapper = {
                0:":",
                1:";",
                2:".",
                3:".",
                4:"#",
                5:"A",
                6:"*",
        }
        tile_map_strings = []

        for row in tiled_map:
            mapped_row = "".join(mapper[col] for col in row)
            tile_map_strings.append(mapped_row)

        with open(os.path.join(self.path, "tile_map.txt"), 'w') as file:
            for row_str in tile_map_strings:
                file.write(row_str + '\n')

    # Getters and setters
    def get_noise_map(self):
        return self.noise_map

    
    def get_tiled_map(self):
        return self.tile_map


    def get_min_value(self):
        return self.min_val


    def get_max_value(self):
        return self.max_val


    def get_world_name(self):
        return self.world_name



if __name__ == '__main__':
    world = World(1024, 1024, world_name="BLAH")
