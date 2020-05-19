def process(X, Y):
    n = len(X)
    m = len(Y)
    L = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(1, n+1):
        L[i][0] = i + 1
    for j in range(1, m+1):
        L[0][j] = j + 1

    for  i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]
            else :
                L[i][j] = min(L[i-1][j], L[i][j-1], L[i-1][j-1]) + 1
    
    return L[n][m]

if __name__ == "__main__":
    X = 'aec'
    Y = 'bcd'
    print(process(X, Y))
