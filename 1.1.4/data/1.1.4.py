import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
data_np = data.to_numpy()

n = 0
values = set()
all20 = []
pairs = []
for i in range(len(data_np)):
    for j in range(len(data_np[i])):
        n += 1
        values.add(data_np[i][j])
        all20.append(data_np[i][j])
print(len(all20))
N_2 = 0
for i in values:
    N_2 += all20.count(i)
for i in values:
    pairs.append([i, all20.count(i) / N_2])

data40 = pd.read_csv("40s.csv")
data40_np = data40.to_numpy()
n40 = 0
values40 = set()
all40 = []
pairs40 = []
for i in range(len(data40_np)):
    for j in range(len(data40_np[i])):
        n40 += 1
        values40.add(data40_np[i][j])
        all40.append(data40_np[i][j])
print(len(all40))
N_2 = 0
for i in values40:
    N_2 += all40.count(i)
for i in values40:
    pairs40.append([i, all40.count(i) / N_2])

x = all40
y = all20

x_label = "$n$"
y_label = "$\omega_n$"
title = ""
fig1, ax1 = plt.subplots()
ax1.hist(y, bins = 28, density=True, color = "#7663b0", alpha = 0.75, label = "20s")
ax1.set_ylabel(y_label)
ax1.set_xlabel(x_label)
ax1.set_title(title)
ax1.legend(loc = 'upper left')
plt.savefig('../pictures/20s.png', transparent=1)
plt.show()

fig2, ax2 = plt.subplots()
ax2.hist(x, bins = 35, density=True, color = "#539caf", alpha = 1, label = "40s")
# ax2.set_ylabel(y_label)
# ax2.set_xlabel("", labelpad = 8.0)
ax2.set_title(title)
ax2.legend(loc = 'upper right')
plt.savefig('../pictures/40s.png', transparent=1)
plt.show()
