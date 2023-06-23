n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input())))
mx = min(n,m)
for i in range(mx-1,-1,-1):
    for j in range(n-i):
        for k in range(m-i):
             if a[j][k] == a[j][k+i] and a[j][k] == a[j+i][k] and a[j][k] == a[j+i][k+i]:
                print((i+1)*(i+1))
                exit(0)
