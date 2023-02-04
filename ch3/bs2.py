k, n = map(int,input().split())
a = []
for _ in range(k):
    tmp = int(input())
    a.append(tmp)
cnt = 0
b = max(a)
while cnt!=n and b!=0:
    cnt = 0
    for x in a:
       cnt += x//b
    if cnt == n:
        print(b)
        break
    elif cnt > n:
        b = b//2