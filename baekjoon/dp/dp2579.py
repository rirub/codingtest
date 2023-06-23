n = int(input())
a = [0]
dp = [0]*(n+1)
for _ in range(n):
    a.append(int(input()))
if n==1:
    print(a[1])
elif n==2:
    print(a[1]+a[2])
else:
    dp[1] = a[1]
    dp[2] = a[1] + a[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+a[i], dp[i-3]+a[i-1]+a[i])

    print(dp[n])