def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        return
    else:
        for i in range(1,n+1):
            if a[v][i]==1 :
                if check[i]==0:
                    check[i] = 1
                    dfs(i)
                    check[i]=0



if __name__=="__main__":
    n, m = map(int,input().split())
    a = [ [0]*(n+1) for _ in range(n+1)]
    check = [0] * (n+1)
    check[1] =1
    for _ in range(m):
        x, y = map(int,input().split())
        a[x][y]=1
    cnt = 0
    dfs(1)
    print(cnt)