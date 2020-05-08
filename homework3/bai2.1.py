def binary(a):
    if a < 2: return str(a)
    return (binary(a//2)) + str(a%2) 

import numpy as np
import time

pln = np.random.randint(low = 1, high = 1000000000, size = 10)
pln.sort()
pltime = []

for a in pln:
    start_time = time.time()
    print(a)
    print("bin a : ", binary(a))
    end_time = time.time()
    pltime.append(float(end_time - start_time))

import matplotlib.pyplot as plt

plt.plot(pln, pltime)
plt.xticks(pln)
plt.savefig("bai2.1.png") 