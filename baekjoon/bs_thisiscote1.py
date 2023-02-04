def Count(len):
    total = 0
    for x in a:
        if x >= len:
            total += x-len
    return total

n, m = map(int,input().split())
a = list(map(int,input().split()))
lt = 0
rt = max(a)

res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
