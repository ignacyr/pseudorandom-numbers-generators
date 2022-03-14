import numpy as np


def rand_sawtooth_linear(x0, n):  # linear pseudorandom number generator with sawtooth signal
    z = 7
    x = np.zeros(n+1)
    x[0] = x0
    for i in range(n):
        x[i + 1] = x[i] * z - np.floor(x[i] * z)
    return x[1:]


def rand_linear(x0, n):      # linear congruential generator
    m = 1.0
    c = 5
    a = np.array([8, 2, 53, 12])
    k = a.size
    x = np.zeros(n + k)
    x[0:k] = x0
    for i in range(n):
        x[i + k] = np.mod(np.sum(a * x[i:(i + k)]) + c, m)
    return x[k:]


def rand_2x(x0, n):   # pseudorandom number generator - probability density: 2x
    m = 10
    c = 15
    a = np.array([8, 2, 53, 12])
    k = a.size
    x = np.zeros(n + k)
    x[0:k] = x0
    for i in range(n):
        x[i + k] = np.mod(np.sum(a * x[i:(i + k)]) + c, m)
    return np.sqrt(x[1:])


def rand_x_plus_1(x0, n):  # pseudorandom number generator - probability density: x + 1 for (-1,0); -x + 1 for [0,1)
    m = 1.0
    c = 5
    a = np.array([8, 2, 53, 12])
    k = a.size
    x = np.zeros(n + k)
    x[0:k] = x0
    for i in range(n):
        x[i + k] = np.mod(np.sum(a * x[i:(i + k)]) + c, m)
    x = x[k:]
    x = x - 0.5
    x[x < 0] = np.sqrt(2*x[x < 0] + 1) - 1
    x[x >= 0] = -np.sqrt(1 - 2*x[x >= 0]) + 1
    print(x)
    return x
