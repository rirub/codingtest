
def Count(len):
    cnt = 1
    ep = Line[0]
    # 마지막에 말을 배치한 지점
    for i in range(1, n):
        if Line[i]-ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int,input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
# 정렬했으니까 가장 큰 값이 배열의 마지막 값

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res= mid
        lt = mid+1
    else:
        rt = mid-1
print(res)