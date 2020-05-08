def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2) 

import numpy as np
import time

pln = np.random.randint(low = 1, high = 30, size = 10)
pln.sort()
pltime = []

for n in pln:
    start_time = time.time()
    print (n)
    print("fib n-th :" , fib(n))
    end_time = time.time()
    pltime.append(float(end_time - start_time))

import matplotlib.pyplot as plt

plt.plot(pln, pltime)
plt.xticks(pln)
plt.savefig("bai2.3.png") 