def dfs(v):
    global cnt
    if v == 0:
        cnt += 1
        return
    else:
        for i in range(n):
            if a[i][v]==1 and check[i]==0:
                check[i] = 1
                dfs(i)
                check[i]=0



if __name__=="__main__":
    n, m = map(int,input().split())
    a = [ [0]*n for _ in range(n)]
    check = [0] * n
    for _ in range(m):
        x, y = map(int,input().split())
        a[x-1][y-1]=1
    cnt = 0
    dfs(n-1)
    print(cnt)