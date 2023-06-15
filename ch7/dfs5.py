def dfs(L, a, b, c):
    global res
    if L == n:
        if a!= b and b!=c and a!=c:
            tmp = (max(a,b,c)-min(a,b,c))
            if tmp<res:
                res = tmp
                return
    else:
        dfs(L+1,a+v[L],b,c)
        dfs(L+1,a,b+v[L],c)
        dfs(L+1,a,b,c+v[L])

if __name__=="__main__":
    n = int(input())
    v = []
    res = 2147000000
    for _ in range(n):
        x = int(input())
        v.append(x)
    dfs(0,0,0,0)
    print(res)
