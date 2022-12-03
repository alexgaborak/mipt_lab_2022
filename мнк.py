import numpy as np
# import matplotlib.pyplot as plt
# x_data = np.arange(-2, 2.01, 0.001)
# n = 20
# b = 0.5
# a = 3
# y_data = np.array([])
# y = np.array([])
# for x in x_data:
#     for i in range(n):
#         y = np.append(y, np.cos(np.pi*x*a**i)*b**i)
#     y_sum = np.sum(y)
#     y_data = np.append(y_data, y_sum)
#     y = np.array([])
#
# plt.plot(x_data, y_data)
# plt.axis('equal')
# plt.grid = True
# plt.show()
x = [0.442011004, 0.490347313,	0.513968477,	0.548598231,	0.599656288,	0.655335938,	0.737406605,	0.829495251,	0.891393812,	0.936099287]
y = [0.008109003,	0.054779402,	0.075652502,	0.106961703,	0.158443803,	0.211646003,	0.291654003,	0.375830303,	0.436987103,	0.485878703]
p, v = np.polyfit(x, y, deg=1, cov=True)
print(p)
print(v)