import sys
input = sys.stdin.readline
from collections import deque

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        sys.exit(0)
    board = []
    for _ in range(h):
        board.append(list(map(int,input().split())))
    dx = [-1, -1, -1, 0, 0, 1,1,1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    Q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j]==1:
                board[i][j]=0
                Q.append((i,j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(8):
                        x = tmp[0]+dx[k]
                        y = tmp[1]+dy[k]
                        if 0<=x<h and 0<=y<w and board[x][y]==1:
                            board[x][y]=0
                            Q.append((x,y))
                cnt += 1
    print(cnt)
