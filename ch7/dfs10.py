import sys
def DFS(x,y):
    if x == 0:
        print(y)
        sys.exit()
    else:
        for i in range(3):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<10 and 0<=yy<10 and a[xx][yy]==1:
                a[xx][yy]=0
                DFS(xx,yy)
                a[xx][yy]=1

if __name__=="__main__":
    a = [list(map(int, input().split())) for _ in range(10)]
    dx = [0,0,-1]
    dy = [-1,1,0]
    for i in range(10):
        if a[9][i]==2:
            a[8][i]=0
            DFS(8,i)
