
import numpy as np
def maze(i):
    for v in range(0,n):
        if(matrix[x[i-1]][v] == 1 and visited[v] == False):
            x[i] = v
            visited[v] = True
            if(x[i] == f-1):
                for j in range(0,i):
                    print(x[j]+1, end='-')
                print(f)
            else:
                maze(i+1)
            visited[v] = False    


matrix=[[0,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,1,1],
        [0,1,0,0,0,1,1,0],
        [0,0,0,0,1,1,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,1,0,0,1,0],
        [0,1,1,0,0,1,0,0],
        [1,1,0,0,0,0,0,0]]
# matrix1=[np.random.randint(low=0,high =2,size=n) for j in range(n)]
n= len(matrix)
visited = [False]*n
f = n-1
x = [0]*n
for i in matrix:
    print(i)
maze(1)