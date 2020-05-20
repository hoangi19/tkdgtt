# Tìm số cách chia tập n phần tử thành phân hoạch k tập con

def count_partition(n, k):
    a = [[0 for i in range(k + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        a[i][0] = 0
    for i in range(k + 1):
        a[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (j == 1 or i == j):
                a[i][j] = 1
            else:
                a[i][j] = (j * a[i - 1][j] + a[i - 1][j - 1])

    return a[n][k]  # kết quả

print(count_partition(3, 2))
# {1, 2, 3} có thể được chia thành các phân hoạch có 2 tập con như sau
# {{1, 2}, 3} {1, {2, 3}}, {{1, 3}, 2}