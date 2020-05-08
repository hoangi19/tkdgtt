#Tính a^n mod c
#Với n nhỏ, ta hoàn toàn có thể giải quyết với chi phí O(n)
#Tuy nhiên với n lớn thì chi phí là rất đẳt
#Bởi vậy chúng ta dùng chia để trị, giảm mức chi phí xuống còn O(log(n))
#Ở bài toán này, chúng ta chọn a nhỏ và c = 1e8+7 để tránh tràn dữ liệu
#(tất nhiên bạn có thể nâng nó nên vì python có big int, nhưng mình chưa test nên có thể sinh lỗi nào đấy :> )

def exp(a, n, c):
    if n == 0: return 1
    sqr = lambda x : (x**2)%c
    if n%2 == 0:
        return sqr(exp(a, n//2, c)) %c
    else :
        return a*(sqr(exp(a, n//2, c)) %c ) %c

print("5^1000000000000000000 mod (100000007)")
print(exp(5, 1000000000000000000, 1e8+7))
