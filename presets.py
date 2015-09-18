import random as Rand
#instensity, height, scale-x, engine, R, G, B, coloursharpness, slope division (only valid when using engine 8)

original1 = [50, 300, 1, 1, 10, 128, 15, 1]
original2 = [10, 300, 1, 0, 10, 128, 15, 1]
original3 = [10, 300, 1, 8, 10, 128, 15, 1]
plains = [1, 100, 5, 8, 10, 128, 15, 1]
mountains = [30, 150, 1, 0, 110, 110, 110, 1]
random_terrain = [Rand.randint(1, 25), Rand.randint(10, 750), Rand.randint(1, 25), Rand.randint(0, 8), Rand.randint(0, 255), Rand.randint(0, 255), Rand.randint(0, 255), Rand.randint(0, 10)]
downslopes = [1, 400, 1, 2, 100, 220, 250, 1]
upslopes = [1, 10, 1, 3, 100, 220, 250, 1]
iceplains = [1, 300, 5, 0, 100, 220, 250, 1]
hills = [5, 300, 5, 5, 0, 200, 64, 1]
volcanism = [100, 250, 2.5, 5, 50, 30, 40, 10]
spires = [60, 30, 2, 7, 124, 101, 64, 1]
rollinghills = [10, 300, 1, 8, 10, 128, 15, 1]
pinkhills = [10, 99, 1, 8, 240, 110, 190, 1]
bloodspires = [50, 300, 1, 6, 75, 15, 20, 5]
mesa = [10, 300, 1, 6, 201, 65, 0, 10]
