#Backtracking : Quay lui
#Bài toán:  Cho 1 mảng a nxm phần tử. 
#           Biết rằng trên mỗi ô có biểu thị các số nguyên. 
#           Nếu a[i][j] > 0 thì ô được phép đi qua, < 0 ô bị chặn, = 0 điểm 1, 1 hoặc điểm n, m
#           Bạn chỉ được đi sang phải hoặc xuống dưới so 1 ô so với ô hiện tại
#           Tìm 1 đường đi bất kỳ từ 1,1 đến n,m thoả mãn
#Cách làm:  Ở 1 đỉnh i,j ta có 2 lựa chọn hoặc đi xuống i+1,j hoặc đi sang i,j+1.
#           Ta đến thử từng ô kề để xem có thể đi tiếp từ ô hiện tại không, nếu không thì quay lại
#Độ phức tạp O(2^(n+m))

def printTrace(trv, u, v):
    if trv[u][v][0] < 0:
        print(u+1, ",", v+1, " -> ", end=" ")
        return
    printTrace(trv, trv[u][v][0], trv[u][v][1])
    print(u+1, "," , v+1, " -> ", end=" ")

def dfs(x, y, matrix, trv):
    global n, m
    if x == n and y == m:
        printTrace(trv, n, m)
        print("end!!")
        return True

    if x > n or y > m:
        return False
    if y < m:
        if matrix[x][y+1] >= 0:
            trv[x][y+1] = x, y
            if dfs(x, y+1, matrix, trv):
                return True
    if x < n:
        if matrix[x+1][y] >= 0:
            trv[x+1][y] = x, y
            if dfs(x+1, y, matrix, trv):
                return True
    return False


#Test
n, m = 4, 6
matrix = [
    [0, 1, 3, -1, -1, -1],
    [3, 3, 1, -1, -1, 2],
    [-1, 2, 1, 2, 2, -1],
    [2, 2, -1, 2, 3, 0]
]

trv = [[[0, 0] for i in range(m)] for j in range(n)]
trv[0][0] = -1, -1
n = n-1
m = m-1
if not dfs(1, 1, matrix, trv):
    print("No answer!")