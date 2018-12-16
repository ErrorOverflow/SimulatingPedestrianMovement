import random
import Graph
import numpy

walkers = [[0 for num in range(2)] for loc in range(24)]
# 5-8 5-8
i = 0
isFill = 0
while i < 24:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    for j in range(i):

    if (isFill != 1):
        walkers[i][0] = x * 0.03 + 5
        walkers[i][1] = y * 0.03 + 5
        i += 1
    else:
        continue

for num in range(24):
    print(walkers[num][0], walkers[num][1])

ui = Graph.UI(24)
ui.init(walkers)
ui.run()
