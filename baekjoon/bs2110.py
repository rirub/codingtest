def Count(len):
    cnt = 1
    ep = a[0]
    for i in range(1,n):
        if a[i]-ep >= len:
            cnt += 1
            ep = a[i]
    return cnt

n, c = map(int,input().split())
a = []
for _ in range(n):
    tmp = int(input())
    a.append(tmp)
a.sort()
# 배치할 수 있는 값은 1부터 배열의 마지막 원소의 값
lt = 1
rt = a[n-1]
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1


print(res)