n = int(input())
a = [ list(map(int,input().split())) for _ in range(n)]

m = int(input())
for i in range(m):

    x,y,z = map(int, input().split())
    tmp = a[x][0:-1]

    if y == 0:
        for _ in range(z):
            a[x-1].append(a[x-1].pop(0))
    else:
        for _ in range(z):
            a[x-1].insert(0,a[x-1].pop(0))
res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s,e+1):
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1

print(res)