def dfs(n):
    if len(res)==m:
        for x in res:
            print(x, end=' ')
        res.pop()
        return
    else:
        res.append(a[n])
        dfs(0)
        dfs(1)
        dfs(2)


if __name__=="__main__":
    n, m = map(int,input().split())
    a = list(range(1,n+1))
    dfs(0)
    res = []