from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

ch = [[0]*n for _ in range(n)]
ch[n//2][n//2]=1
sum = 0
Q = deque()
Q.append((n//2,n//2))
sum += a[n//2][n//2]
L = 0

while True:
    if L==n//2:
        break
    else:
        size = len(Q)
        for j in range(size):
            tmp = Q.popleft()
            for i in range(4):
                x = tmp[0]+dx[i]
                y = tmp[1]+dy[i]
                if ch[x][y] == 0:
                    ch[x][y]=1
                    sum += a[x][y]
                    Q.append((x,y))
                    L+=1

print(sum)