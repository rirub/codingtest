def DFS(x,y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<n and 0<=yy<n and a[x][y]<a[xx][yy]:
                DFS(xx,yy)



if __name__=="__main__":
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    min = 2147000000
    max = -2147000000
    sx=0
    sy=0
    ex=0
    ey=0

    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]<min:
                min = a[i][j]
                sx = i
                sy = j
            if a[i][j]>max:
                max = a[i][j]
                ex = i
                ey = j
    DFS(sx,sy)
    print(cnt)