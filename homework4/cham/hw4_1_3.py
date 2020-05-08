# Liet ke cac day nhi phan co do dai n
n = int(input("Day nhi phan co do dai n = "))
a = [0]*n #list a co n phan tu gia tri 0
def lietke(i): 
    for v in [0,1]:
        a[i] = v
        if i==n-1:
            print(*a)
        else:
            lietke(i+1)
lietke(0)

