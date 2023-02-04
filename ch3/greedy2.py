n = int(input())
a = []
for _ in range(n):
    h,w = map(int,input().split())
    a.append((h,w))
a.sort(reverse=True)
cnt = 1
weight = a[0][1]
for i in range(1,n):
    if a[i][1]>weight:
        cnt +=1
        weight = a[i][1]
print(cnt)