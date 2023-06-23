from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    a = [[0]*m for _ in range(n)]
    Q = deque()
    cnt = 0
    for _ in range(k):
        x,y = map(int,input().split())
        a[y][x]=1
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                a[i][j]=0
                cnt += 1
                Q.append((i,j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        xx = tmp[0]+dx[k]
                        yy = tmp[1]+dy[k]
                        if 0<=xx<n and 0<=yy<m and a[xx][yy]==1:
                            a[xx][yy]=0
                            Q.append((xx,yy))
    print(cnt)