#tìm tổ tiên
def find_root(u):
    global root
    if root[u] == -1:
        return u
    return find_root(root[u])

def kruskal(matrix):
    n = len(matrix[0])

    ans = 0
    global root
    #make and sort edges
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                edges.append((matrix[i][j], i, j ))
    edges.sort()
    
    for edge in edges:
        w, u, v = edge
        root_u = find_root(u)
        root_v = find_root(v)
        # nối u vs v có tạo thành chu trình ko
        if root_u != root_v:
            if root_u < root_v:
                root[root_v] = root_u
            else:
                root[root_u] = root_v
            ans = ans + w
            print(u, "-", v, " : ", w)
    
    print("Cây khung tối thiểu có tổng trọng số : ", ans)

# đồ thị vô hướng, liên thông
matrix = [  [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

#tổ tiên tại i
root = len(matrix[0])*[-1]

kruskal(matrix)