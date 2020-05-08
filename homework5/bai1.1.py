def money(x, m):
    mid = m.copy()
    m.sort( reverse = True )
    
    ans = (len(m))*[0]
    for val in m:
        ans[mid.index(val)] = x//val
        x = x%val
    if x != 0: return -1
    return ans

#các mệnh giá tiền đang có
m = [1, 2, 5, 10, 20, 50, 100, 200, 500]
x = 1542 #tổng tiền cần trả
print(money(x, m))