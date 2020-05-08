prime = {}
def era(n):
    for i in range(n+1):
        prime[i] = 1
    prime[0] = prime[1] = 0
    for i in range(n+1):
        if prime[i] == 1:
            print(i)
            for j in range(i+i, n+1, i):
                prime[j] = 0
n = int(input("Enter n : "))
era(n)
