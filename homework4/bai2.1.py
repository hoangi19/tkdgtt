
def permutation(arr):
    #nếu chỉ 1 phần tử thì hiển nhiên chỉ có 1 hoán vị
    if len(arr) <= 1:
        return [arr]

    res = []

    #với từng phần tử trong mảng, ta tìm tất cả hoán vị với phần tử đó là phần tử đầu tiên trong hoán vị
    for i in range(len(arr)):
        node_mid = arr[i]
        next_per = arr[:i] + arr[i+1:]
        
        #tìm hoán vị của n - 1 thành phần còn lại trong mảng
        for per in permutation(next_per):
            res.append([node_mid] + per)
    
    return res

#Test
arr = [1, 2, 3, 4]
print(*permutation(arr), sep="\n")