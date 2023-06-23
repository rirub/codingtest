T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    dy = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        dy[0][i]=i

    for i in range(1,k+1):
        for j in range(1,n+1):
            sum = 0
            for l in range(1,j+1):
                sum+=dy[i-1][l]
            dy[i][j]=sum
    print(dy[k][n])

