def count(a,h):
    sum = 0
    for i in a:
        if i<h:
            sum += i
        else:
            sum += h
    return sum
n = int(input())
a = list(map(int,input().split()))
m = int(input())
a.sort()
result = 0

if sum(a)<=m:
    print(max(a))
else:
    s = min(a)
    e = max(a)
    while s<=e:
        mid = (s+e)//2
        if count(a, mid) > m:
            e = mid-1
        else:
            if result < mid:
                result = mid
                s = mid + 1

    print(result)
