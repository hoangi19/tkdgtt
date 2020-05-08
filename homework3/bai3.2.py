def min_max(a, left, right):
    if left >= right : return a[left], a[left]
    mid = (right + left)//2
    minL, maxL = min_max(a, left, mid-1)
    minR, maxR = min_max(a, mid+1, right)
    return min(minL, minR), max(maxL, maxR)
import numpy as np
import time

pln = np.random.randint(low = 100, high = 10000, size = 10)
pln.sort()
pltime = []

for n in pln:
    a = np.random.randint(low = 1, high = 100000000, size = n)
    # v = a[np.random.randint(low = 0, high = n, size = 1)]
    start_time = time.time()
    print("a: ", a)
    # print("v: ", v)
    print(min_max(a, 0,  n-1))
    end_time = time.time()
    pltime.append(float(end_time - start_time))
print(pltime)
import matplotlib.pyplot as plt

plt.plot(pln, pltime)
plt.xticks(pln)
plt.savefig("bai3.2.png") 