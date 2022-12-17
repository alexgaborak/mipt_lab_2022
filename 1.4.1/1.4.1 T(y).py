import numpy as np
import matplotlib.pyplot as plt
from math import *

from scipy.optimize import curve_fit  # function for fitting data with a curve


# # mport numpy as np #work with arrays and linear algebra
# # import matplotlib.pyplot as plt #plot diagrams
# # Fitting function with its argument a and two parameters
def fit_func(y, a, b):
    return pi / 5 * np.sqrt((a + np.square(y)) / (9.8 * (b + y)))


# # Data
z = np.linspace(0, 70, 10000)
y = [9.005, 23.405, 27.505, 32.705, 39.805, 46.005, 54.005, 61.305, 66.105, 69.705]
T = [1.4556, 1.4122, 1.4156, 1.4256, 1.4422, 1.4674, 1.5062, 1.553, 1.5816, 1.6]
# Fitting procedure returning params values and covariation matrix.
# Consumes fitting function, data and initial parameters values
params, cov = curve_fit(fit_func, y, T)
# create figure where to draw plots
plt.figure(figsize=(8, 5))
# #define titles and axis limits
plt.title("Зависимость периода колебаний от расстояния до центра масс груза")
y = np.array(y)
T = np.array(T)
plt.errorbar(y, T, xerr=0.5, yerr=0.5 / 100 * T, label='T(y)', color='green', linestyle='', linewidth=5)
plt.ylabel("T, s")
plt.xlabel("y, cm")
plt.ylim(1.35, 1.65)  # limit on T axis
# plot fitting function
plt.plot(z, fit_func(z, params[0], params[1]))
# print parameter values and their errors
print("M =" + str(round(params[0], 3)) + "+-" +
      str(round(np.sqrt(cov[0][0]), 3)) + " kg")
print("m = " + str(round(params[1], 3)) + "+-" +
      str(round(np.sqrt(cov[1][1]), 3)) + " kg")
# show figure while running script interactively


# save figure
plt.savefig("T(y)+fun.png")
plt.show()
