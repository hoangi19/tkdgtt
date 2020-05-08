def printSol(a):
    print(a)

def Try(k, a, x):
    if k == len(x):
        return
    for i in range(k,min(k+a+1, len(x)+1)):
        printSol(x[k:i])
    Try(k+1, a, x)
    
x = [1, 2, 3]
T = 1

Try(0, T+1, x)

