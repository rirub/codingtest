def dfs(L, s):
    if L==k:
        if s>0:
            res.add(s)
    else:
        dfs(L+1, s+a[L])
        dfs(L+1,s-a[L])
        dfs(L+1, s)


if __name__ == "__main__":
    k = int(input())
    a = list(map(int,input().split()))
    res = set()
    dfs(0,0)
    print(res)
    print(sum(a)-len(res))

