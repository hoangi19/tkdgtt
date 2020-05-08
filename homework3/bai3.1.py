def find(a, value, left, right):
    if left >= right : return False
    mid = (right + left)//2
    if a[mid] == value: return True
    if a[mid] < value: return find(a, value, mid+1, right)
    return find(a, value, left, mid-1)
import numpy as np
import time

pln = np.random.randint(low = 100, high = 10000, size = 10)
pln.sort()
pltime = []

for n in pln:
    a = np.random.randint(low = 1, high = 100000000, size = n)
    v = a[np.random.randint(low = 0, high = n, size = 1)]
    start_time = time.time()
    a.sort()
    print("a: ", a)
    print("v: ", v)
    print(find(a, v, 0,  n-1))
    end_time = time.time()
    pltime.append(float(end_time - start_time))
print(pltime)
import matplotlib.pyplot as plt

plt.plot(pln, pltime)
plt.xticks(pln)
plt.savefig("bai3.1.png") 