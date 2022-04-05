from generators import rand_sawtooth_linear, rand_linear, \
    rand_2x_sawtooth, rand_2x, rand_pyramid_sawtooth, rand_pyramid, \
    rand_exp_sawtooth, rand_exp, rand_laplace_sawtooth, rand_laplace
import matplotlib.pyplot as plt
import numpy as np


def main():
    quantity = 5000

    random_numbers = rand_sawtooth_linear(0.79911312515, quantity)
    random_numbers_2 = rand_exp(np.array([0.7155645, 0.54564, 0.54546, 0.134545]), quantity)

    plt.figure(1)
    plt.hist(random_numbers, bins=100)
    plt.xlabel("Wartość próbki")
    plt.ylabel("Ilość próbek")

    plt.figure(2)
    plt.hist(random_numbers_2, bins=100)
    plt.xlabel("Wartość próbki")
    plt.ylabel("Ilość próbek")

    plt.figure(3)
    plt.plot(random_numbers, '.')
    plt.xlabel("Numer próbki")
    plt.ylabel("Wartość próbki")
    plt.grid(True)

    plt.figure(4)
    plt.plot(random_numbers_2, '.')
    plt.xlabel("Numer próbki")
    plt.ylabel("Wartość próbki")
    plt.grid(True)

    plt.figure(5)
    ax = plt.axes(projection='3d', proj_type='ortho')
    ax.plot3D(random_numbers[0::2],
              random_numbers[1::2],
              np.linspace(0, int(quantity/2)-1, int(quantity/2)), '.')
    plt.xlabel("Wartość A")
    plt.ylabel("Wartość B")

    plt.figure(6)
    ax = plt.axes(projection='3d', proj_type='ortho')
    ax.plot3D(random_numbers_2[0::2],
              random_numbers_2[1::2],
              np.linspace(0, int(quantity/2)-1, int(quantity/2)), '.')
    plt.xlabel("Wartość A")
    plt.ylabel("Wartość B")

    plt.figure(7)
    plt.plot(random_numbers[0::2], random_numbers[1::2], '.')
    plt.xlabel("Wartość A")
    plt.ylabel("Wartość B")
    plt.grid(True)

    plt.figure(8)
    plt.plot(random_numbers_2[0::2], random_numbers_2[1::2], '.')
    plt.xlabel("Wartość A")
    plt.ylabel("Wartość B")
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    main()
