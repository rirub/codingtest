from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
Q = deque()
Q.append((n//2,n//2))

ch = [[0]*n for _ in range(n)]
ch[n//2][n//2]=1
sum=0
sum += ch[n//2][n//2]
L = 0

while True:
    if L==n//2:
        break
    else:
        tmp = Q.popleft()
        for i in range(4):
            x = tmp[0]+dx[i]
            y = tmp[1]+dy[i]
            if 0<=x<n and 0<=y<n and ch[x][y]==0:
                ch[x][y]=1
                Q.append((x,y))
                sum += a[x][y]
                L += 1
print(sum)