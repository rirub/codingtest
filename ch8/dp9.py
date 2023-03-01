n = int(input())
a = [[0]*(n+1)]
for i in range(1,n+1):
    a.append(list(map(int,input().split())))
    a[i].insert(0,0)
dy=[[0]*(n+1) for _ in range(n+1)]

dy[1][1]=a[1][1]
for i in range(2,n+1):
    dy[1][i]=dy[1][i-1]+a[1][i]
    dy[i][1]=dy[i-1][1]+a[i][1]

for i in range(2,n+1):
    for j in range(2,n+1):
        dy[i][j]=min(dy[i][j-1],dy[i-1][j])+a[i][j]
print(dy[n][n])