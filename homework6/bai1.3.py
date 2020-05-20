def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()

def find_path(A):
    m = len(A)
    n = len(A[0])
    C = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if (i < m):
                C[i][j] = max(C[i - 1][j - 1], C[i][j - 1], C[i + 1][j - 1]) + A[i - 1][j - 1]
            else:
                C[i][j] = max(C[i - 1][j - 1], C[i][j - 1]) + A[i - 1][j - 1]

    print_matrix(C)

    i = m
    j = n
    result = []
    while (j > 0):
        result.append([i - 1, j - 1])
        if (i > 0):
            k = C[i][j] - A[i - 1][j - 1]
            if (C[i - 1][j - 1] == k):
                i -= 1
                j -= 1
            elif (C[i][j - 1] == k):
                j -= 1
            else:
                if (i < m) and C[i + 1][j - 1] == k:
                    i += 1
                    j -= 1

    result.reverse()

    print("Đường đi trên ma trận ban đầu")
    print(result)
    print("Tổng đường đi lớn nhất là", C[m][n])

A = [[9, 9, 9, 2, 6, 1, 6],
     [4, 5, 2, 1, 4, 5, 1],
     [2, 3, 9, 8, 1, 3, 4],
     [5, 7, 2, 1, 9, 8, 1],
     [9, 8, 2, 1, 4, 7, 6],
     [3, 7, 1, 3, 6, 8, 1]]

find_path(A)