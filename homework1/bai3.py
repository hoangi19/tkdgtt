lists = [1, 2, 3, 4, 5]
matrix = [[2,3], [1], [4], [1,2,3,5], []]
res = lists[0]
for u in lists:
    if len(matrix[u-1]) > len(matrix[res-1]):
        res = u
print(res)