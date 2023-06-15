dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt += 1
        return
    else:
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 <= 6 and 0<=y1<=6 and a[x][y] == 0:
                a[x1][y1] = 1
                DFS(x1,y1)
                a[x1][y1] = 0








if __name__=="__main__":
    a = [ list(map(int,input().split())) for _ in range(7)]
    cnt = 0
    a[0][0]=1
    DFS(0,0)
    print(cnt)