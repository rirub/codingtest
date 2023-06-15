from collections import deque
board = [list(map(int,input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]
distance = [[0]*7 for _ in range(7)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
Q = deque()
Q.append((0,0))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            distance[x][y]=distance[tmp[0]][tmp[1]]+1
            Q.append((x,y))

if distance[6][6]==0:
    print(-1)
else:
    print(distance[6][6])





Q = deque()
Q.append((0,0))
