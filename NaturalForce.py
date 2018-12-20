import sys

sys.setrecursionlimit(100000000)
GUIDE = [[[9999.0 for x_loc_num in range(2)] for y_loc_num in range(1100)] for z_loc_num in range(1300)]
LOC_INIT = [1246, 689]
GUIDE[LOC_INIT[0]][LOC_INIT[1]][0] = 0
GUIDE[LOC_INIT[0]][LOC_INIT[1]][1] = 999
NATURE_ALPHA = 0.05


def isOutofBounder(loc):
    if 933 <= loc[0] <= 991 and 632 <= loc[1] <= 750:
        return 0
    elif 341 <= loc[0] <= 1246 and (1028 - 53) <= loc[1] <= 1028:
        return 0
    elif 341 <= loc[0] <= 394 and 321 <= loc[1] <= 1028:
        return 0
    elif 341 <= loc[0] <= 1246 and 321 <= loc[1] <= 374:
        return 0
    elif (1246 - (394 - 341)) <= loc[0] <= 1246 and 739 <= loc[1] <= 1028:
        return 0
    elif (1246 - (394 - 341)) <= loc[0] <= 1246 and 321 <= loc[1] <= 639:
        return 0
    return 1


def nature_init(loc):
    a, b, c, d, e, f, g, h = [0 for _ in range(2)], [0 for _ in range(2)], [0 for _ in range(2)], [0 for _ in
                                                                                                   range(2)], [0 for _
                                                                                                               in range(
            2)], [0 for _ in range(2)], [0 for _ in range(2)], [0 for _ in range(2)]
    a[0] = b[0] = h[0] = loc[0] - 1
    c[0] = g[0] = loc[0]
    d[0] = e[0] = f[0] = loc[0] + 1
    b[1] = c[1] = d[1] = loc[1] + 1
    a[1] = e[1] = loc[1]
    h[1] = g[1] = f[1] = loc[1] - 1

    #print(a[0], a[1])
    if isOutofBounder(b) and GUIDE[b[0]][b[1]][0] > GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5:
        GUIDE[b[0]][b[1]][0] = GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5
        GUIDE[b[0]][b[1]][1] = 5
        nature_init(b)
    if isOutofBounder(h) and GUIDE[h[0]][h[1]][0] > GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5:
        GUIDE[h[0]][h[1]][0] = GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5
        GUIDE[h[0]][h[1]][1] = 3
        nature_init(h)
    if isOutofBounder(a) and GUIDE[a[0]][a[1]][0] > GUIDE[loc[0]][loc[1]][0] + 1:
        GUIDE[a[0]][a[1]][0] = GUIDE[loc[0]][loc[1]][0] + 1
        GUIDE[a[0]][a[1]][1] = 4
        nature_init(a)

    if isOutofBounder(c) and GUIDE[c[0]][c[1]][0] > GUIDE[loc[0]][loc[1]][0] + 1:
        GUIDE[c[0]][c[1]][0] = GUIDE[loc[0]][loc[1]][0] + 1
        GUIDE[c[0]][c[1]][1] = 6
        nature_init(c)
    if isOutofBounder(g) and GUIDE[g[0]][g[1]][0] > GUIDE[loc[0]][loc[1]][0] + 1:
        GUIDE[g[0]][g[1]][0] = GUIDE[loc[0]][loc[1]][0] + 1
        GUIDE[g[0]][g[1]][1] = 2
        nature_init(g)

    if isOutofBounder(d) and GUIDE[d[0]][d[1]][0] > GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5:
        GUIDE[d[0]][d[1]][0] = GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5
        GUIDE[d[0]][d[1]][1] = 7
        # nature_init(d)
    if isOutofBounder(e) and GUIDE[e[0]][e[1]][0] > GUIDE[loc[0]][loc[1]][0] + 1:
        GUIDE[e[0]][e[1]][0] = GUIDE[loc[0]][loc[1]][0] + 1
        GUIDE[e[0]][e[1]][1] = 0
        # nature_init(e)
    if isOutofBounder(f) and GUIDE[f[0]][f[1]][0] > GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5:
        GUIDE[f[0]][f[1]][0] = GUIDE[loc[0]][loc[1]][0] + 2 ** 0.5
        GUIDE[f[0]][f[1]][1] = 1
        # nature_init(f)


def nature_force(loc):  # 二维数组，如{5.44,6.32}
    force = [0.00 for i in range(2)]
    if GUIDE[loc[0]][loc[1]][1] == 0:
        force[0] = -NATURE_ALPHA
    elif GUIDE[loc[0]][loc[1]][1] == 1:
        force[1] = NATURE_ALPHA
    elif GUIDE[loc[0]][loc[1]][1] == 2:
        force[0] = NATURE_ALPHA
    elif GUIDE[loc[0]][loc[1]][1] == 3:
        force[1] = -NATURE_ALPHA
    return force


nature_init(LOC_INIT)
print(nature_force([618, 618]))
