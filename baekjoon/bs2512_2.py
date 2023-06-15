n = int(input())
a = list(map(int,input().split()))
m = int(input())

if sum(a)<=m:
    print(max(a))
else:
    a.sort()
    lt = a[0]
    rt = a[n-1]
    res = 0
    while lt<=rt:
        mid = (lt+rt)//2
        sum = 0
        for x in a:
            if x < mid:
                sum += x
            else:
                sum += mid
        if sum > m:
            rt = mid-1
        else:
            res = mid
            lt = mid +1
    print(rt)
