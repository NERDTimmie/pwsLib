import os
import numpy as np
import perlin as perlin
import json
import sys


# World
class World:

    def __init__(self):
        self.world_array = np.zeros((200, 200, 200), np.int8)

    def setBlock(self, x, y, z, t):
        self.world_array[x][z][y] = t

    def getBlock(self, x, y, z):
        return self.world_array[x][z][y]

    def export(self):
        filename, file_extension = os.path.splitext(sys.argv[0])
        with open(filename + ".json", "w") as f:
            print("{\"world\":" + json.dumps(self.world_array.tolist()) + "}", file=f)


def perlinmap():
    perlin_array = perlin.generate_perlin_noise_2d((160, 160), (5, 5))
    return perlin_array


def random():
    return np.random.rand()
