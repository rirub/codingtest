def dfs(x, y):
    global cnt
    if y==m:
        cnt += 1
        for i in range(1,n+1):
            if ch[i]!=0:
                print(i, end =' ')
                ch[i]-=1
        print()
        return
    else:
        dfs(x, y+1)
        dfs(x+1,y+1)
        dfs(x+1, y)



if __name__=="__main__":
    n, m = map(int,input().split())
    ch = [0] * (n+1)
    cnt = 0
    dfs(0,0)
    print(cnt)