a = [7, 8, 9]
n = len(a)
b = [0]*n
visited = [False]*n
def hoanvi(i):
    # global visited
    for v in range(0,n):
        if visited[v] == False:
            b[i] = v
            visited[v] = True
            if i == n - 1:
                for j in b:
                    print(a[j], end = " ")
                print()
            else:
                hoanvi(i+1)
            visited[v] = False
hoanvi(0)