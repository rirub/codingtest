N = int(input())

arr = [0] * (N+1)
cnt = 0

for i in range(2,N+1):
    if arr[i]==0:
        cnt += 1
        for j in range(i, N+1, i):
            arr[j] = 1
print(cnt)