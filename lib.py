import numpy as np


def distance(x, y):
    return np.sqrt(np.sum(np.square(x - y)))
