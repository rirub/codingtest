import sys

def DFS(L, sum):
    if L==n:
        if sum==F:
            for j in range(n):
                print(res[j], end=' ')
            sys.exit()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] =i
                # sum += i * cl[L]
                DFS(L+1, sum+(i * cl[L]))
                ch[i] = 0

if __name__=="__main__":
    n, F = map(int,input().split())
    cl = [1] * (n)
    for i in range(1,n-1):
        cl[i] = cl[i-1] * (n-i) // i
    print(cl)
    ch = [0] * (n+1)
    res = [0] * n
    DFS(0,0)