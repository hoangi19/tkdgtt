
#cho biết xâu gồm l ký tự kết thúc tại Xi có trùng với xâu l ký tự liên trước không
def same(i, l, X):
    j = i - l
    for k in range(l):
        if X[i-k] != X[j-k]:
            return False
    return True

#cho biết Xi có làm hỏng tính lặp của dãy X1 X2..Xi hay không
def check(i, X):
    for l in range(1, i//2 + 1):
        if same(i, l, X):
            return False
    return True

#Giữ kết quả tốt nhất
def keepRes(T, X):
    global minC, res, N
    minC = T[N]
    res = X.copy()

#Thử các giá trị có thể của Xi
def Try(i, X):
    global minC, N
    for j in ['A', 'B', 'C']:
        X[i] = j
        if check(i, X): #Nếu thêm giá trị vào thoả mãn
            if j == 'C':
                T[i] = T[i-1]+1
            else:
                T[i] = T[i-1]
            if T[i] + (N-i)//4 < minC: #Đánh giá nhánh cận
                if i == N:
                    keepRes(T, X)
                else:
                    Try(i+1, X)

#Test
N = 10
#min C trong xâu kết quả, khởi tạo là N, giá trị tệ nhất 
minC = N
#tổng C từ 1 -> i
T = (N+1)*[0]
#mảng kết quẩ
res = (N+1)*['']
#mảng thử
X = (N+1)*['']
Try(1, X)
print(*res[1:], sep="")
print("min C : ", minC)