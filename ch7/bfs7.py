from collections import deque

m,n = map(int,input().split())
a = []
Q = deque()
result = -2147000000
days = 0
for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
ch = [ [0]*m for _ in range(n) ]
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            days=0
            a[i][j]=-1
            ch[i][j] =1
            Q.append((i,j))
        while Q:
            tmp = Q.popleft()
            for k in range(4):
                ii = tmp[0]+dx[k]
                jj = tmp[1]+dy[k]
                if 0<=ii<n and 0<=jj<m and a[ii][jj]==0:
                    a[ii][jj]=1
                    ch[ii][jj]=1
                    Q.append((ii,jj))
            if Q:
                days +=1
        if days>result:
            result = days
print(result)