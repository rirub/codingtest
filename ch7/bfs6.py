from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = -2147000000
Q = deque()

minx = 101
maxx = 1

for i in range(n):
    for j in range(n):
        if a[i][j]<minx:
            minx = a[i][j]
        if a[i][j]>maxx:
            maxx = a[i][j]
# print(minx, maxx)

for x in range(minx,maxx):
    cnt = 0
    ch = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]>x and ch[i][j]==0:
                cnt += 1
                ch[i][j]=1
                Q.append((i,j))
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        ii = tmp[0]+dx[k]
                        jj = tmp[1]+dy[k]
                        if 0<=ii<n and 0<=jj<n and a[ii][jj]>x and ch[ii][jj]==0:
                            ch[ii][jj]=1
                            Q.append((ii,jj))

    if cnt > result:
        result = cnt
print(result)
