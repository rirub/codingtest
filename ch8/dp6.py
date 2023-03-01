n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dy = [0]*(n+1)
res = 0
for i in range(1,n+1):
    max = 0
    for j in range(i-1, 1, -1):
        if a[i] > a[j] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res = dy[i]
print(res)