#Cho đồ thị vô hướng có trọng số G
#Tìm đường đi ngắn nhất từ U đến V trên đồ thị

import queue

def printTrace(trace, x):
    if trace[x] == -1:
        print(x , "->", end="")
        return
    printTrace(trace, trace[x])
    print(x, "->", end="")

def process(matrix, u, v):
    n = len(matrix)
    f = n*[1e8+7]
    f[u] = 0
    pq = queue.PriorityQueue()
    mark = n*[-1]
    pq.put((0, u))

    while not pq.empty() :
        w, i = pq.get()
        for j in range(n):
            # print(i, j)
            if matrix[i][j] != 0:
                if f[j] > w+matrix[i][j]:
                    f[j] = w + matrix[i][j]
                    mark[j] = i
                    pq.put((f[j], j))
    
    print("Min : ", f[v])
    printTrace(mark, v)
    print("end")
    pass


# đồ thị vô hướng
matrix = [  [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
u = 0
v = 4

process(matrix, u, v)