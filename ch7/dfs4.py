def DFS(L, sum):
    global cnt
    if sum>T:
        return
    if sum == T:
        cnt += 1
        return
    if L == k:
        if sum != T:
            return
    else:
        for i in range(a[L][1]+1):
            DFS(L+1, sum+(a[L][0]*i))



if __name__=="__main__":
    T = int(input())
    k = int(input())
    a = list()
    for _ in range(k):
        x, y = map(int,input().split())
        a.append((x,y))
    cnt = 0
    a.sort(reverse=True)
    DFS(0,0)
    print(cnt)