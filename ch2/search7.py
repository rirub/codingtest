n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
center = n-1//2
for i in range(n):
    for j in range(center-i,center+i+1):
        sum += a[i][j]