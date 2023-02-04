def DFS(L):
    if L == m:
        global cnt
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt +=1
        return
    else:
        if L==0:
            for i in range(1, n+1):
                res[L]=i
                check[i]=1
                DFS(L+1)
                check[i]=0
        else:
            for i in range(res[L-1]+1, n+1):
                if check[i]==0:
                    res[L]=i
                    check[i]=1
                    DFS(L+1)
                    check[i]=0

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    check = [0] * (n+1)
    DFS(0)
    print(cnt)