n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
res = [0]*n

for i in range(1,n+1):
    for j in range(n):
        if a[i]==0 and res[j]==0:
            res[j]=i
            break
        elif res[j]==0:
            a[i]-=1
for x in res:
    print(x,end=' ')

