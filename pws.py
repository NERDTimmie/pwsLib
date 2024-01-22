import numpy as np
import perlin as perlin
import json


# World
class World:

    def __init__(self):
        self.world_array = np.zeros((50, 50, 100), np.int8)

    def setBlock(self, x, y, z, t):
        self.world_array[x][y][z] = t

    def getBlock(self, x, y, z):
        return self.world_array[x][y][z]

    def export(self):
        with open("output.json", "w") as f:
            print(json.dumps(self.world_array.tolist()), file=f)


def perlinmap():
    perlin_array = perlin.generate_perlin_noise_2d((50, 50), (5, 5))
    return perlin_array


def random():
    return np.random.rand()
