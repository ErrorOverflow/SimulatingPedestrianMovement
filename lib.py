import numpy as np


def distance(x, y):
    return (pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)) ** 0.5


def length(x):
    return (pow(x[0], 2) + pow(x[1], 2)) ** 0.5
