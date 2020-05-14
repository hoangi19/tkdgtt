#Bố trí phòng họp

#truy vết
def printTrace(trace, i, time):
    if trace[i] == -1:
        print(time[i], end=" ")
        return
    printTrace(trace, trace[i], time)
    print(time[i], end=" ")

def process(time):
    time.sort()
    n = len(time)
    F = (n+1)*[1]
    trace = (n+1)*[-1]
    for i in range(0, n):
        for j in range(i, -1, -1):
            if time[j][1] <= time[i][0]:
                if F[i] < F[j]+1:
                    F[i] = F[j]+1
                    trace[i] = j       
    print("Ans : ", max(F))
    printTrace(trace, F.index(max(F)), time)


time = [
    [2, 5],
    [1, 3],
    [13, 16],
    [4, 7],
    [5, 9],
    [8, 10],
    [11, 14]
]

process(time)