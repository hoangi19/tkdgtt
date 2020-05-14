#Balo 0-1

def process(W, V, m):
    W = [0] + W
    V = [0] + V
    n = len(W)
    F = [[-1 for x in range(m+1)] for y in range(n)]  #bảng phương án + rào mảng
    
    #Cơ sở qhđ
    for i in range(0, n):                               
        F[i][0] = 0
    for j in range(0, m+1):
        F[0][j] = 0
    
    # print(*F, sep="\n")

    for i in range(1, n):
        for j in range(0, m+1):
            if j >= W[i]:
                F[i][j] = max(F[i-1][j-W[i]] + V[i], F[i][j])
            F[i][j] = max(F[i-1][j], F[i][j])
    ans = F[n-1][m]
    print("Ans : ", ans)
    #truy vết
    for i in range(n-1, -1, -1):
        if F[i][m] != F[i-1][m]:
            print(i, end=" ")
            m = m - W[i]
W = [3, 4, 5, 9, 4]
V = [3, 4, 4, 10, 5]
m = 11
process(W, V, m)