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

y_label = " $ n, \ 20 \ c $ "
x_label = "$ \omega_n$"
title=""
# plt.figure(figsize=(8, 6), dpi=160)
fig1, ax1 = plt.subplots()
ax1.hist(y, bins=28, density=True, orientation='horizontal', color="black", alpha=0.75, label="20s")
ax1.set_ylabel(y_label)
ax1.set_xlabel(x_label)
ax1.set_title(title)
ax1.legend(loc='upper right')

y_label = "$n, \ 40 \ c$"
x_label = "$\omega_n$"
ax2 = ax1.twinx()
plt.hist(x, bins=35, density=True, orientation='horizontal', color="#539caf", alpha=0.5, label="40s")
ax2.set_ylabel(y_label)
ax2.set_xlabel(x_label)
ax2.set_title(title)
ax2.legend(loc='lower right')
plt.savefig('../pictures/histogram.png', dpi=300, transparent=1)
plt.show()
