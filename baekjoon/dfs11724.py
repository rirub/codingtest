import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def DFS(x):
    visited[x] = True
    for i in range(1,n+1):
        if graph[x][i]==1:
            if visited[i]==False:
                graph[x][i]=0
                graph[i][x]=0
                DFS(i)

if __name__=="__main__":
    n, m = map(int,input().split())
    graph = [ [0]*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)
    cnt = 0
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x][y]=1
        graph[y][x]=1

    for i in range(1,n+1):
        if visited[i]==False:
            DFS(i)
            cnt += 1
    print(cnt)