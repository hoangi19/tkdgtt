import numpy as np

def search(a, v):
    return np.where(a == v)

pln = np.random.randint(1000000, high=10000000, size=5)
pln.sort()
pltime = []

import time
for n in pln:
    a = np.random.randint(-100, high=100, size=n)
    v = np.random.randint(-100, high=100, size=1)
    start_time = time.time()
    search(a, v)
    end_time = time.time()
    pltime.append(float(end_time - start_time))

import matplotlib.pyplot as plt

plt.xticks(pln)
plt.plot(pln, pltime)
# plt.show()
plt.savefig("bai2.png")     