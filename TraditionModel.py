import random
import Graph
import lib
import numpy as np
import time


def init():
    walkers = [[0.00 for num in range(2)] for loc in range(24)]
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
isKill = [0.00 for num in range(24)]


def gravity(loc):  # 驱动力
    grav = [0.00 for i in range(2)]
    if loc[0] >= 9.91:
        x_bias = 12.46 - loc[0]
        y_bias = (7.39 + 6.39) / 2 - loc[1]
        z_bias = np.sqrt(np.square(x_bias) + np.square(y_bias))
        grav[0] = x_bias / z_bias * 0.2
        grav[1] = y_bias / z_bias * 0.2
    elif 9.33 <= loc[0] < 9.91:
        grav[0] = 0.2
        grav[1] = 0
    else:
        if loc[1] >= (7.50 + 6.32) / 2:
            x_bias = 9.33 - loc[0]
            y_bias = (7.50 + 0.3) - loc[1]
            z_bias = np.sqrt(np.square(x_bias) + np.square(y_bias))
            grav[0] = x_bias / z_bias * 0.2
            grav[1] = y_bias / z_bias * 0.2
        else:
            x_bias = 9.33 - loc[0]
            y_bias = (6.32 - 0.3) - loc[1]
            z_bias = np.sqrt(np.square(x_bias) + np.square(y_bias))
            grav[0] = x_bias / z_bias * 0.2
            grav[1] = y_bias / z_bias * 0.2
    return grav


def illegal_judge(loc, force):  # 墙排斥
    if (9.33 - 0.2) <= loc[0] <= 9.91 and (6.32 - 0.2) <= loc[1] <= (7.50 + 0.2):
        if loc[0] <= 9.33:
            force[0] = 0
            force[1] = (loc[1] - (6.32 + 7.50) / 2) * random.random() * 0.05
        else:
            force[1] = 0
            force[0] += random.random() * 0.05
        return force
    return force


def avoid_hit(force, pre_v, num):  # 行人碰撞
    near = [0.00 for i in range(2)]
    i = 0
    while i < 24:
        if i == num:
            i += 1
            continue
        if lib.distance(pre_v, location[i]) <= 0.4:
            near[0] += (location[i][0] - pre_v[0])
            near[1] += (location[i][1] - pre_v[1])
        i += 1
    near[0] *= -1
    near[1] *= -1
    z_bias = np.sqrt(np.square(near[0]) + np.square(near[1]))
    if z_bias == 0:
        return force
    force[0] = (force[0] / 0.1 + near[0] / z_bias) * 0.05
    force[1] = (force[1] / 0.1 + near[1] / z_bias) * 0.05
    return force


def kill(loc, num):
    if loc[0] >= (12.46 - (3.94 - 3.41)):
        isKill[num] = 1
    return 0


def move(force, pre_v, num):  # 调用上面的函数确定行人到底往哪走
    now = [0.00 for i in range(2)]
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    if force[0] == 0 and force[1] <= 0.01:
        force[1] = (pre_v[1] - (6.32 + 7.50) / 2) * random.random() * 0.2
    force = avoid_hit(force, pre_v, num)
    force = illegal_judge(now, force)
    now[0] = pre_v[0] + force[0]
    now[1] = pre_v[1] + force[1]
    return now


ui = Graph.UI(24)
ui.barrier()
for round in range(2000):
    ui.delete()
    for i in range(24):  # 依次挪动24个行人
        kill(location[i], i)
        if isKill[i]:
            location[i] = [15, 8]
            continue
        force = gravity(location[i])
        location[i] = move(force, location[i], i)
    ui.init(location)
    ui.barrier()
    time.sleep(0.2)
