n = int(input())
a = [[0]*(n+1)]
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    a.append(tmp)
    a[i].insert(0,0)
print(a)