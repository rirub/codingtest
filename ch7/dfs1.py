def dfs(s,t):
    if t>m:
        return
    elif t==m:
        res.append(s)
        return
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                dfs(s+a[i][0],t+a[i][1])
                ch[i]=0

if __name__=="__main__":
    n,m = map(int,input().split())
    a = []
    res = []
    for _ in range(n):
        x, y = map(int,input().split())
        a.append((x,y))
        a.sort(key=lambda x:(x[1]))
    ch = [0]*n

    dfs(0,0)

    print(max(res))