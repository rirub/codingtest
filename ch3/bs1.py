n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
left = 0
right = n-1
while left<=right :
    mid = (left + right) // 2
    if m==a[mid]:
        print(mid+1)
        break
    elif m<a[mid]:
        right=mid-1
    elif m>a[mid]:
        left = mid+1


