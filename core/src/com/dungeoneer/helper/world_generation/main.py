from perlin_noise import PerlinNoise
import sys
import secrets


class World():
    
    # size_x and size_y are the numnber of tiles in the world in the x and y axes respectively
    def __init__(self, size_x, size_y, random_seed):
        self.generate_noise_map(size_x, size_y, random_seed)

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
    
    def get_noise_map(self):
        return self.noise_map
    
    def get_min_value(self):
        return self.min_val
    
    def get_max_value(self):
        return self.max_val


def generate_map_seed(length=16):

    alphabet = "0123456789"
    return int(''.join(secrets.choice(alphabet) for _ in range(length)))


if __name__ == '__main__':
    
    """
    
    1. A string of 8 characters: 012345678 [each character has a range between 0 and and 9]
        Correspondence:
            # [0] MOUNTAINS
            # [1] PEAKS
            # [2] DEPTH1
            # [3] DEPTH2
            # [4] DEPTH3
            # [5] FIELD
            # [6] EDGE
    2. SIZE_X
    3. SIZE_Y

    """

    for i in range(0, len(sys.argv)):
        print(f"{sys.argv[i]}")

    random_seed = generate_map_seed()
    world = World(256, 256, random_seed)
