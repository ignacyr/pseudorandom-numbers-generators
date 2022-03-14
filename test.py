from generators import rand_sawtooth_linear, rand_linear, \
    rand_2x_sawtooth, rand_2x, rand_pyramid_sawtooth, rand_pyramid, \
    rand_exp_sawtooth, rand_exp, rand_laplace_sawtooth, rand_laplace
import matplotlib.pyplot as plt
import numpy as np

quantity = 100000

random_numbers_sawtooth = rand_laplace_sawtooth(0.79911312515, quantity)
random_numbers_2 = rand_laplace(np.array([0.7155645, 0.54564, 0.54546, 0.134545]), quantity)
random_numbers = np.random.rand(quantity)

plt.figure(1)
plt.hist(random_numbers_sawtooth, bins=100)

plt.figure(2)
plt.hist(random_numbers_2, bins=100)
#
# plt.figure(3)
# plt.hist(random_numbers, bins=100)

# plt.figure(4)
# plt.plot(random_numbers_sawtooth, '.')
#
# plt.figure(5)
# plt.plot(random_numbers_2, '.')
#
# plt.figure(6)
# plt.plot(random_numbers, '.')
#
# plt.figure(7)
# ax = plt.axes(projection='3d', proj_type='ortho')
# ax.plot3D(random_numbers_sawtooth[0::2],
#           random_numbers_sawtooth[1::2],
#           np.linspace(0, int(quantity/2)-1, int(quantity/2)), '.')
#
# plt.figure(8)
# ax = plt.axes(projection='3d', proj_type='ortho')
# ax.plot3D(random_numbers_2[0::2],
#           random_numbers_2[1::2],
#           np.linspace(0, int(quantity/2)-1, int(quantity/2)), '.')
#
# plt.figure(9)
# ax = plt.axes(projection='3d', proj_type='ortho')
# ax.plot3D(random_numbers[0::2],
#           random_numbers[1::2],
#           np.linspace(0, int(quantity/2)-1, int(quantity/2)), '.')

plt.show()
