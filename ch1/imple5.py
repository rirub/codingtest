n, m = map(int, input().split())
arr = [0] * (n+m+1)
max = 0
result = []
for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i+j] +=1

for idx, x in enumerate(arr):
    if x > max:
        result = []
        result.append(idx)
        max = x
    elif x == max:
        result.append(idx)
for i in result:
    print(i, end=' ')
