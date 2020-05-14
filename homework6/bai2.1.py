#Đổi tiền

def process(D, m):
    n = len(D)
    #Bảng phương án + rào mảng
    F = (m+10)*[1e8+7] 
    
    #cơ sở qhđ
    for d in D:
        F[d] = 1
    
    for j in range(0, m+1):
        for d in D:
            if j > d:
                F[j] = min(F[j], F[j-d]+1)

    #truy vết
    if F[m] != 1e8+7:
        print(F[m])

        while F[m] != 1:
            for d in D:
                if F[m-d] == F[m]-1:
                    print(d, end=" ")
                    m = m - d
                    break
        print(m)
    else:
        print(-1)

D = [2, 6, 5]
m = 1
process(D, m)