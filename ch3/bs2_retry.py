k,n = map(int,input().split())
List = []
res = 0

def Count(len):
    cnt = 0
    for x in List:
        cnt += (x//len)
    return cnt
for _ in range(n):
    tmp = int(input())
    List.append(tmp)

lt = 1
rt = max(List)

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)