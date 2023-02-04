def DFS(L,s):
    global cnt
    tmp = 0
    if L==k:
        for j in range(k):
            tmp += res[j]
        if tmp % m == 0:
            cnt +=1
    else:
        for i in range(s,n):
            res[L]=a[i]
            DFS(L+1,i+1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0,0)
    print(cnt)