def underPrime(x):
    pCnt = 0
    tmp = x
    while tmp>1:
        for i in range(2,x):
            if (tmp%i) == 0:
                tmp = tmp//i
                pCnt += 1
                break
    print(pCnt)
    if p[pCnt]==1:
        return 1
    else:
        return 0



if __name__=="__main__":
    A,B = map(int,input().split())
    cnt = 0
    p = [0]*(B+1)
    for i in range(2,B+1):
        if p[i]==0:
            p[i]=1
            for j in range(i+1,B+1):
                if j%i==0:
                    p[j]=999
    for i in range(A,B+1):
        cnt += underPrime(i)
    print(cnt)