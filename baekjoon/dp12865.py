
N,k = map(int,input().split())
bag = []
for _ in range(N):
    w, v = map(int,input().split())
    bag.append((w,v))

dy = [0]*(k+1)

for i in range(N):
    for j in range(k,bag[i][0]-1,-1):
        dy[j]=max(dy[j],dy[j-bag[i][0]]+bag[i][1])

print(dy[k])