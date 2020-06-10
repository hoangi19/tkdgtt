# Cho đồ thị G
# Hãy tô màu các đỉnh của đồ thị sao cho 2 đỉnh có đường đi trực tiếp đến nhau không có cùng màu và số màu dùng là bé nhất

def process(matrix):
    n_color = 0
    n = len(matrix)
    color = n*[-1]
    for i in range(n):
        if color[i] == -1:
            n_color = n_color + 1
            for j in range(n):
                if color[j] == -1 and matrix[i][j] == 0:
                    color[j] = n_color
    
    print(color)
    pass

# đồ thị G
matrix = [  [0, 1, 0, 1, 0], 
            [1, 0, 1, 1, 1], 
            [0, 1, 0, 0, 1], 
            [1, 1, 0, 0, 1], 
            [0, 1, 1, 1, 0]] 

process(matrix)