from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
Q = []
board = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
Q = deque(Q)
distance = [[0]*(m) for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i,j))

while Q:
    tmp = Q.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<n and 0<=y<m and board[x][y]==0:
            board[x][y]=1
            distance[x][y] = distance[tmp[0]][tmp[1]] +1
            Q.append((x,y))
for i in range(n):
    if 0 in board[i]:
        print(-1)
        sys.exit(0)
else:
    mx = 0
    for i in range(n):
        if mx < max(distance[i]):
            mx = max(distance[i])
    print(mx)