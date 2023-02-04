n,m = map(int,input().split())
Music = list(map(int,input().split()))
lt = max(Music)
rt = sum(Music)
res = 0
def Count(len):
    cnt = 0
    tmp = len
    for x in Music:
        tmp -= x
        if tmp <= 0:
            cnt +=1
            tmp = len-x
    return cnt


while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)<=m:
        res = mid
        rt = mid-1
    elif Count(mid)>m:
        lt = mid+1


print(mid)