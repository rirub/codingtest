
def dfs(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i]=1
                res[L]= i
                dfs(L + 1)
                ch[i]=0


if __name__=="__main__":
    n, m = map(int,input().split())
    a = list(range(1,n+1))
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    dfs(0)
    print(cnt)
