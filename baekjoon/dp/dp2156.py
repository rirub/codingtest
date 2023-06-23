import sys
input = sys.stdin.readline
n = int(input())
a = []
dp = [0]*n

for _ in range(n):
    x = int(input())
    a.append(x)
if n==1:
    dp[0]=a[0]
elif n==2:
    dp[1]=a[0]+a[1]
elif n==3:
    dp[2]=max(a[0]+a[1],a[0]+a[2],a[1]+a[2])
else:
    dp[0] = a[0]
    dp[1] = a[0] + a[1]
    dp[2] = max(a[0]+a[1],a[0]+a[2],a[1]+a[2])
    for i in range(3,n):
        dp[i]=max(dp[i-2]+a[i], dp[i-3]+a[i-1]+a[i])
print(max(dp))