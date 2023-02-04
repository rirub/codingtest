n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

lt = 0
rt = n-1

while lt<=rt:
    mid=(lt+rt)//2
    if m==a[mid]:
        print(mid+1)
        break
    elif m<a[mid]:
        rt=mid-1
    elif m > a[mid]:
        lt = mid+1
