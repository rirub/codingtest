def DFS(L,sum):
    global res
    if L==n+1:
        if res<sum:
            res = sum
            return
    if L>n:
        return

    else:
        DFS(L+t[L],sum+p[L])
        DFS(L+1, sum)


if __name__=="__main__":
    n = int(input())
    t = []
    p = []
    for _ in range(n):
        a,b = map(int, input().split())
        t.append(a)
        p.append(b)
    res = -2147000000
    DFS(0,0)
    print(res)