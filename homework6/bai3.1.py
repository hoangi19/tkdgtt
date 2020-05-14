# Cho một dãy n số nguyên a1, a2, ..., an, ai nguyên dưong. Hãy tìm hai chỉ số i, j sao cho i < j và hiệu aj - ai là lớn nhất.

# input: một mảng số nguyên dương.
# output : giá trị lớn nhất của aj - ai

def hieuso(a:[]):

    mina = a[1]
    ans = -1
    for i in range(len(a)):
        ans = max(a[i]-mina, ans)
        mina = min(mina, a[i])
    return ans

if __name__ == "__main__":
    a = [2, 5, 1, 3]
    print(hieuso(a))