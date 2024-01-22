import os
import numpy as np
import perlin as perlin
import json
import sys


# World
class World:

    def __init__(self):
        self.world_array = np.zeros((50, 50, 100), np.int8)

    def setBlock(self, x, y, z, t):
        self.world_array[x][y][z] = t

    def getBlock(self, x, y, z):
        return self.world_array[x][y][z]

    def export(self):
        filename, file_extension = os.path.splitext(sys.argv[0])
        with open(filename + ".json", "w") as f:
            print("{\"world\":")
            print(json.dumps(self.world_array.tolist()), file=f)
            print("}")


def perlinmap():
    perlin_array = perlin.generate_perlin_noise_2d((50, 50), (5, 5))
    return perlin_array


def random():
    return np.random.rand()
