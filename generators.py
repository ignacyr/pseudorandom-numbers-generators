import numpy as np


def rand_sawtooth_linear(x0, n):
    z = 7
    x = np.zeros(n+1)
    x[0] = x0
    for i in range(n):
        x[i + 1] = x[i] * z - np.floor(x[i] * z)
    return x[1:]


def rand_linear(x0, n):      # rand_2
    m = 10
    c = 15
    a = np.array([8, 2, 53, 12])
    k = a.size
    x = np.zeros(n + k)
    x[0:k] = x0
    for i in range(n):
        x[i + k] = np.mod(np.sum(a * x[i:(i + k)]) + c, m)
    return x[k:]


# def rand_2x(x0, n):
#
#
#
