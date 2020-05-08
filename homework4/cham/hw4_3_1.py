n = 4
k = 3
visited = [False]*n
a = []
b = [0]*n
def chinhhop(i):
    global a, c
    if k <= n:
        for v in range(0,n):
            # a.append(v)
            if (visited[v] == False):
                b[i] = v + 1
                visited[v] = True
                if i == k:
                    c = []
                    for j in range(0, k):
                        c += [b[j]]               
                    if(c not in a):
                        a += [c]
                else:
                    chinhhop(i+1)
                visited[v] = False
    else:
        return False
chinhhop(0)
print(*a)
