from math import *
from scipy.optimize import curve_fit #function for fitting data with a curve
import numpy as np #work with arrays and linear algebra
import matplotlib.pyplot as plt #plot diagrams
#Fitting function with its argument a and two parameters
def fit_func(y, M, m):
    return 2*pi*np.sqrt((M+np.square(y))/(100*9.8*(m+y)))


# # Data
z = np.linspace(0, 70, 1000)
y = [9.005,	23.405,	27.505,	32.705,	39.805,	46.005,	54.005,	61.305,	66.105,	69.705]
T = [1.4556, 1.4122, 1.4156, 1.4256, 1.4422, 1.4674,	1.5062,	1.553, 1.5816, 1.6]
# Fitting procedure returning params values and covariation matrix.
#Consumes fitting function, data and initial parameters values
params, cov = curve_fit(fit_func, y, T, p0 = [30, 1.5])
#create figure where to draw plots
plt.figure(figsize=(8,5))
#define titles and axis limits
plt.title("Зависимость периода колебаний от расстояния до центра масс")
a = np.array(y)
T = np.array(T)
plt.errorbar(a,T,xerr=0.5, yerr=0.5/100*T,label='T(a)',color='green', linestyle='', linewidth=5)
plt.ylabel("T, s")
plt.xlabel("a, cm")
plt.ylim(1.4, 1.7) #limit on T axis
#plot fitting function
plt.plot(z, fit_func(z, params[0], params[1]))
#print parameter values and their errors
print("T_min ="+ str(round(params[0], 3))+ "+-"+
str(round(np.sqrt(cov[0][0]), 3))+" s")
print("a_0 = "+str(round(params[1], 3))+"+-"+
str(round(np.sqrt(cov[1][1]), 3))+" cm")
#show figure while running script interactively




#save figure
plt.savefig("T(a)+fun.png")
plt.show()





m=np.array([57, 92, 92, 92, 92, 92, 116, 142, 180, 219, 273, 341, 74])
om = np.array([0.034522996, 0.057119866, 0.056605273, 0.056861405, 0.057643902, 0.056861405, 0.072220521, 0.087672353, 0.112199738, 0.135413476, 0.169054313, 0.212989332, 0.046370371])
plt.scatter(om*1000, m)
plt.show()