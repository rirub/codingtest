n = int(input())
a = [ list(map(int,input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    tmp = []
    x,y,z = map(int, input().split())
    tmp = a[x]
    print(tmp)
    # if y == 0:
    #     for i in range(y):
    #         a[x][n-1-i] = tmp[i]
    #     for j in range(z,n):
    #         a[x][j-y] = tmp[j]
    # elif y == 1:
    #     for k in range(n-1-z):
    #         a[x][k+3] = tmp[k]
    #     for l in range(n-1-z,z):
    #         a[x][l-n-3] = tmp[l]


print(a)