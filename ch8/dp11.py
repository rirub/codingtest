n = int(input())
a = list(map(int,input().split()))
m = int(input())

dy = [501]*(m+1)
for x in a:
    dy[x]=1

for i in a:
    for j in range(i+1,m+1):
        dy[j]=min(dy[j], dy[j-i]+dy[i])
        print(dy)
print(dy[m])