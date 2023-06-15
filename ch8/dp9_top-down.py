def DFS(x,y):
    if dy[x][y]!=0:
        return dy[x][y]
    else:
        tmp = min(DFS(x-1,y), DFS(x,y-1))
        dy[x][y]+=tmp+a[x][y]



if __name__=="__main__":
    n = int(input())
    a = [[0]*(n+1)]
    for i in range(1,n+1):
        a.append(list(map(int,input().split())))
        a[i].insert(0,0)
    dy = [[0]*(n+1) for _ in range(n+1)]

    print(DFS(n,n))
