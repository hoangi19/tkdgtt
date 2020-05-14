#Dãy con đơn điệu dài nhất

#truy vết
def printTrace(trace, i, A):
    if trace[i] == -1:
        print(A[i], end=" ")
        return
    printTrace(trace, trace[i], A)
    print(A[i], end=" ")

#xử lý
def process(A):
    n = len(A)  
    F = n*[0]   #bảng phương á
    F[0] = 1    #cơ sở qhđ
    trace = n*[-1]  #vết
    for i in range(1, n):
        for j in range(i, -1, -1):
            if A[i] > A[j]:
                if F[i] < F[j] + 1:
                    trace[i] = j
                    F[i] = F[j]+1
    
    print("Ans : ", max(F))
    printTrace(trace, i, A)

A = [1, 2, 3, 4, 9, 10, 5, 6, 7]
process(A)