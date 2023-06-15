import sys
input = sys.stdin.readline

def dfs(x,y):
    if x<0 or x>=h or y<0 or y>=w:
        return
    if graph[x][y] == 0:
        return
    else:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)




if __name__=="__main__":
    while True:
        w,h = map(int,input().split())
        if w==0 and h==0:
            sys.exit(0)
        graph = []
        cnt = 0
        for _ in range(h):
            graph.append(list(map(int,input().split())))

        for i in range(h):
            for j in range(w):
                if graph[i][j]==1:
                    dfs(i,j)
                    cnt +=1
        print(cnt)