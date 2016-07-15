import random as Rand
#instensity, height, scale-x, engine, R, G, B, coloursharpness, tree chance

original1 = [50, 300, 1, 1, 10, 128, 15, 1, 100]
original2 = [10, 300, 1, 0, 10, 128, 15, 1, 0]
original3 = [10, 300, 0.1, 8, 10, 128, 15, 1, 0]
plains = [1, 300, 2, 8, 10, 128, 15, 1, 20]
mountains = [30, 300, 1, 8, 80, 80, 80, 1, 10]
forest = [7, 200, 2, 8, 9, 50, 12, 5, 70]
mountains2 = [10, 400, 1, 6, 124, 124, 112, 1, 10]
ice_mountains = [79, 386, 8, 5, 244, 200, 252, 2, 0]
lands_of_clay = [1, 400, 18, 0, 205, 145, 71, 9, 13]
perlin_hills = [20, 300, 1, 11, 20, 115, 25, 3, 3]
varied_perlin_hills = [Rand.randint(1, 40), Rand.randint(200, 500), Rand.randint(1, 5), 11, Rand.randint(0, 50), Rand.randint(0, 205), Rand.randint(0, 50), Rand.randint(0, 10), Rand.randint(0, 20)]
