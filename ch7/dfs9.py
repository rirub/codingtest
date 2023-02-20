def DFS(x,y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and a[xx][yy]==1:
            a[xx][yy]=0
            result[-1]+=1
            DFS(xx,yy)

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int,input())) for _ in range(n)]
    result = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if a[i][j] ==1:
                a[i][j]=0
                result.append(1)
                DFS(i,j)
    print(len(result))
    result.sort()
    for res in result:
        print(res)


