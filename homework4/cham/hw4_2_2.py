
def tohop(i):
    global a, c
    for v in range(0, n):
        if (visited[v]==False):
            b[i]= (v+1)
            visited[v]= True
            if(i==k):
                c = []
                for j in range(0, k):
                    c += [b[j]]
                c = sorted(c)                
                if(c not in a):
                    a += [c]
            else:
                tohop(i+1)
            visited[v] = False
n = 4
k = 2
a= []
visited=[False]*n
b=[0]*n
tohop(0)
print(*a)