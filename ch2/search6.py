n = int(input())
a = []
result = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

diagonal1 = 0
diagonal2 = 0
for i in range(n):
    diagonal1 += a[i][i]
    diagonal2 += a[n-i-1][n-i-1]
result.append(diagonal1)
result.append(diagonal2)
for j in range(n):
    row = 0
    col = 0
    for k in range(n):
        row += a[j][k]
        col += a[k][j]
    result.append(row)
    result.append(col)

print(max(result))

