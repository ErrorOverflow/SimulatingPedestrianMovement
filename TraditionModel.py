import random
import Graph
import lib
import numpy as np


def init():
    walkers = [[0 for num in range(2)] for loc in range(24)]
    # 5-8 5-8
    i = 0
    isFill = 0
    while i < 24:
        loc = np.random.rand(2)
        loc[0] = loc[0] * 3 + 5
        loc[1] = loc[1] * 3 + 5
        for j in range(i):
            if lib.distance(loc, walkers[j]) <= 0.4:
                isFill = 1
                print(lib.distance(loc, walkers[j]))
                break
        if isFill == 1:
            isFill = 0
            continue
        walkers[i] = loc
        i += 1

    return walkers


location = init()
ui = Graph.UI(24)
ui.init(location)
ui.run()
