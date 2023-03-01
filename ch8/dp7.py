n = int(input())
a = []
dy = [0]*(n+1)
res = 0
for _ in range(n):
    area, height, weight = map(int,input().split())
    a.append((area,height, weight))
a.sort(reverse=True)
a.insert(0,(0,0,0))
dy[1]=a[1][1]
for i in range(2,n+1):
    max = 0
    for j in range(i-1,0,-1):
        if a[i][2]<a[j][2] and dy[j]>max:
            max = dy[j]
    dy[i]=max+a[i][1]
    if res < dy[i]:
        res = dy[i]
print(res)