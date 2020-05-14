#Tham khảo : http://ntucoder.net/Problem/Details/5518

def process(n, A):
    F = (n+1)*[0]
    F[0] = 1
    for a in A:
        for j in range(n, -1, -1):
            if j >= a:
                F[j] = max(F[j-a], F[j])
    print(F)

    for j in range(n, -1, -1):
        if F[j] == 1:
            print(j)
            return

n = 7
A = [2, 6, 5]
process(n, A)