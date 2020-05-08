import numpy as np

def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if a[m] > a[j]:
                m = j
        a[m], a[i] = a[i], a[m]
    return a


pln = np.random.randint(1, high=1000, size=5)
pln.sort()
pltime = []

import time
for n in pln:
    a = np.random.randint(-100, high=100, size=n)
    # print(n)
    start_time = time.time()
    a = selection_sort(a)
    end_time = time.time()
    pltime.append(float(end_time - start_time))

import matplotlib.pyplot as plt

plt.plot(pln, pltime)
# plt.show()
plt.savefig("bai1.png")        