n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
# a.sort()
a.sort()

result = [0]*(m)

for i in range(m):
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt+rt)//2
        if a[mid] == b[i]:
            result[i]=1
            break
        elif a[mid]>b[i]:
            rt=mid-1
        elif a[mid]<b[i]:
            lt = mid+1
for x in result:
    print(x, end=' ')