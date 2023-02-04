n,m = map(int,input().split())

a = [[0]*m for _ in range(n)]

for _ in range(m):
    x, y, z = list(map(int, input().split()))
    a[x-1][y-1]=z

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()