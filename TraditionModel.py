import random
import Graph
import lib
import numpy as np
import time


def init():
    walkers = [[0.00 for num in range(2)] for loc in range(24)]
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


def gravity(loc):
    grav = [0.00 for i in range(2)]
    x_bias = 12.46 - loc[0];
    y_bias = (7.39 + 6.39) / 2 - loc[1];
    z_bias = np.sqrt(np.square(x_bias) + np.square(y_bias))
    grav[0] = x_bias / z_bias
    grav[1] = y_bias / z_bias
    return grav


def illegal_judge(loc, force):
    if (loc[0] >= 9.33 and loc[0] <= 9.91 and loc[1] >= 6.32 and loc[1] <= 7.50):
        force[0] = 0
        force[1] += 0.2 * force[0]
        return force
    return force


def move(force, pre_v):
    now = [0.00 for i in range(2)]
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    force = illegal_judge(now, force)
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    return now


location = init()
ui = Graph.UI(24)
ui.barrier()
for round in range(2000):
    ui.delete()
    for i in range(24):
        force = gravity(location[i])
        location[i] = move(force, location[i])
    ui.init(location)
    ui.barrier()
    time.sleep(0.5)
ui.run()
