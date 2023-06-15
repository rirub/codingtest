if __name__=="__main__":
    n = int(input())
    dy = [[999]*(n+1) for _ in range(n+1)]
    res = [999]*(n+1)
    result = []
    for i in range(1,n+1):
        dy[i][0]=0
        dy[0][i]=0
        dy[i][i]=0

    while True:
        n,m = map(int,input().split())
        if n==-1 and m==-1:
            break
        else:
            dy[n][m]=1
            dy[m][n]=1

    for c in range(1,n+1):
        print("포문이 안돌아")
        for a in range(1,n+1):
            for b in range(1,n+1):
                dy[a][b] = min(dy[a][b], dy[a][c]+dy[c][b])

    for i in range(1,n+1):
        print("얘는??")
        res[i]=max(dy[i])

    for i in range(1,n+1):
        if res[i]==min(res):
            result.append(i)

    print(min(res),len(result))
    for x in result:
        print(x,end=' ')
    print("머임????????????")