import numpy as np


def rand_sawtooth_linear(x0, n):  # linear PRNG with sawtooth signal
    z = 7
    x = np.zeros(n+1)
    x[0] = x0
    for i in range(n):
        x[i + 1] = x[i] * z - np.floor(x[i] * z)
    return x[1:]


def rand_linear(x0, n):      # LCG
    m = 1.0
    c = 5
    a = np.array([8, 2, 53, 12])
    k = a.size
    x = np.zeros(n + k)
    x[0:k] = x0
    for i in range(n):
        x[i + k] = np.mod(np.sum(a * x[i:(i + k)]) + c, m)
    return x[k:]


def rand_2x_sawtooth(x0, n):   # PRNG - probability density: 2x
    x = rand_sawtooth_linear(x0, n)
    x = np.sqrt(x)  # inverse CFD
    return x


def rand_2x(x0, n):   # PRNG - probability density: 2x
    x = rand_linear(x0, n)
    x = np.sqrt(x)  # inverse CFD
    return x


def rand_pyramid_sawtooth(x0, n):  # PRNG - probability density: x + 1 for (-1,0); -x + 1 for [0,1)
    x = rand_sawtooth_linear(x0, n)
    x = x - 0.5
    x[x < 0] = np.sqrt(2 * x[x < 0] + 1) - 1  # inverse CFD for x < 0
    x[x >= 0] = -np.sqrt(1 - 2 * x[x >= 0]) + 1  # inverse CFD for x >= 0
    return x


def rand_pyramid(x0, n):  # pseudorandom number generator - probability density: x + 1 for (-1,0); -x + 1 for [0,1)
    x = rand_linear(x0, n)
    x = x - 0.5
    x[x < 0] = np.sqrt(2 * x[x < 0] + 1) - 1  # inverse CFD for x < 0
    x[x >= 0] = -np.sqrt(1 - 2 * x[x >= 0]) + 1 # inverse CFD for x >= 0
    return x
