# Ở 1 vị trí i sẽ có 2 trạng thái, mỗi trạng thái sinh ra 1 số nhị phân có đọ dài n
# Độ phức tạp O(2^n)
def binary_n(n, res, i):
    if i == n:
        print(*res, sep="")
        return
    #trạng thái 0
    res[i] = 0
    binary_n(n, res, i+1)

    #trạng thái 1
    res[i] = 1
    binary_n(n, res, i+1)


#Test
n = 3
res =  [0]*n
binary_n(n, res, 0)