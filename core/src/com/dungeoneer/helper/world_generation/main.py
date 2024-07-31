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
            os.mkdir(self.path + self.world_name)

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


    def create_tile_map_file(self):
        pass 


    # Getters and setters
    def get_noise_map(self):
        return self.noise_map


    def get_min_value(self):
        return self.min_val


    def get_max_value(self):
        return self.max_val


    def get_world_name(self):
        return self.world_name



if __name__ == '__main__':

    """
    1. A string of 8 characters: 012345678 [each character has a range between 0 and and 9]
        >> Correspondence:
            > [0] MOUNTAINS
            > [1] PEAKS
            > [2] DEPTH1
            > [3] DEPTH2
            > [4] DEPTH3
            > [5] FIELD
            > [6] EDGE
    2. SIZE_X
    3. SIZE_Y
    4. World Name
    """

    for i in range(0, len(sys.argv)):
        print(f"{sys.argv[i]}")

    world = World(256, 256, world_name="Testing")
    # noise_map = world.get_noise_map()
