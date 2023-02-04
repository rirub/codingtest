def DFS(total,cnt):
    global result

    if cnt > result:
        return

    if total == target:
        if cnt < result:
            result = cnt
        else:
            return
    elif total > target:
        return

    else:
        for i in range(n):
            DFS(total+a[i],cnt+1)

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    target = int(input())
    result = 2147000000
    DFS(0,0)
    
    print(result)