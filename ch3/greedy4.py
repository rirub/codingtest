n, m =map(int,input().split())
weight = list(map(int,input().split()))
weight.sort()
cnt=0
i = 0
while i<len(weight):
    if len(weight)==i:
        cnt+=1
        break
    if weight[i]+weight[-1]<=m:
        i+=1
    cnt +=1
    weight.pop()
print(cnt)
