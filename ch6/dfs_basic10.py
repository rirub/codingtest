def dfs(L):
    global cnt
    if len(res)==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
        res.pop()
        return
    else:
        for i in range(L, n):
            res.append(a[i])
            dfs(L+1)
        dfs(L+1)




if __name__=="__main__":
    n, m = map(int,input().split())
    a = list(range(1,n+1))
    res = []
    cnt = 0
    dfs(0)

    print(cnt)
