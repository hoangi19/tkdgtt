# đường đi từ A tới B trong mê cung ( đồ thị vô hướng biểu diễn bằng ma trận vuông )

import numpy as np

#in đường đi thu được
def printTrv(trv, u):
    if trv[u] < 0:
        print(u, " -> ", end=" ")
        return
    printTrv(trv, trv[u])
    print(u, " -> ", end=" ")

#Depth first search
def dfs(a, b, matrix, trv, mark):
    if a == b:
        printTrv(trv, b)
        print("end!")
        return True
    if mark[a] == 1:
        return False

    mark[a] = 1
    for v in range(len(matrix[a])):
        if matrix[a][v] == 0 or mark[v] == 1:
            continue
        trv[v] = a
        if dfs(v, b, matrix, trv, mark):
            return True
        trv[v] = 0
    mark[a] = 0

    return False

#Test
#ma trận vuông biểu diễn đồ thị
n = 10
matrix = [[0 for x in range(n)] for y in range(n)] 

#mảng truy vết
trv = [0 for x in range(n)]

#mảng đánh dấu đỉnh đã đi qua
mark = [0 for x in range(n)]

#tạo cạnh giữa các đỉnh
matrix[1][2] = 1
matrix[2][1] = 1
matrix[1][5] = 1
matrix[5][1] = 1
matrix[3][4] = 1
matrix[4][3] = 1
matrix[2][6] = 1
matrix[6][2] = 1


#Test 5 -> 6 : A = 5, B = 6
A = 5
B = 6

#khởi tạo trv[A] = -1 nghĩa là đây là đỉnh đầu tiên của đường đi A -> B
trv[A] = -1

dfs(A, B, matrix, trv, mark)