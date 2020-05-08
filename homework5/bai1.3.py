from queue import PriorityQueue

def prim(matrix):
    n = len(matrix[0])
    mark = n*[0]
    
    q = PriorityQueue()
    q.put((0,0,0))
    ans = 0

    E = []
    while not q.empty():
        w, u, parent = q.get()

        if mark[u] == 1:
            continue
        mark[u] = 1
        ans = ans + w
        E.append(str(parent) + "-" + str(u) + " : " + str(w))
        for v in range(0, n):
            if matrix[u][v] != 0:
                q.put((matrix[u][v], v, u))
    return E[1:]

# đồ thị vô hướng, liên thông
matrix = [  [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
        
print("Cây khung tối thiểu : ", *prim(matrix), sep="\n")
