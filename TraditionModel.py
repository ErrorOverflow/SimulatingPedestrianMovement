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
            if lib.distance(loc, walkers[j]) <= 0.5:
                isFill = 1
                break
        if isFill == 1:
            isFill = 0
            continue
        walkers[i] = loc
        i += 1

    return walkers


location = init()


def gravity(loc):
    grav = [0.00 for i in range(2)]
    x_bias = 12.46 - loc[0]
    y_bias = (7.39 + 6.39) / 2 - loc[1]
    z_bias = np.sqrt(np.square(x_bias) + np.square(y_bias))
    grav[0] = x_bias / z_bias * 0.1
    grav[1] = y_bias / z_bias * 0.1
    return grav


def illegal_judge(loc, force):
    if (loc[0] >= (9.33 - 0.3) and loc[0] <= 9.91 and loc[1] >= (6.32 - 0.3) and loc[1] <= (7.50 + 0.3)):
        if (loc[0] <= 9.33):
            force[0] = 0
            force[1] = (loc[1] - (6.32 + 7.50) / 2) * random.random() * 0.02
        else:
            force[1] = 0
            force[0] += random.random() * 0.02
        return force
    return force


def avoid_hit(force, pre_v, num):
    i = 0
    next = [0.00 for j in range(2)]
    while i < 24:
        next[0] = pre_v[0] + force[0]
        next[1] = pre_v[1] + force[1]
        if i == num:
            continue
        while lib.distance(next, location[i]) <= 0.4:
            print(lib.distance(next, location[i]))
            force[0] = force[0] * 0.8
            force[1] = force[1] * 0.8
            next[0] = pre_v[0] + force[0]
            next[1] = pre_v[1] + force[1]
        i += 1

    return force


def move(force, pre_v, num):
    now = [0.00 for i in range(2)]
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    force = illegal_judge(now, force)
    if force[0] == 0 and force[1] <= 0.01:
        force[1] = (pre_v[1] - (6.32 + 7.50) / 2) * random.random() * 0.2
    #force = avoid_hit(force, pre_v, num)
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    return now


ui = Graph.UI(24)
ui.barrier()
for round in range(2000):
    ui.delete()
    for i in range(24):
        force = gravity(location[i])
        location[i] = move(force, location[i], i)
    ui.init(location)
    ui.barrier()
    time.sleep(0.02)
