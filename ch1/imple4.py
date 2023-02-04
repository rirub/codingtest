import sys

n = int(input())
arr = map(int,  input().split())
avg = round(sum(arr)/n)
min = 2147000000

for idx, x in enumerate(arr):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        res = idx+1
        score = x
    elif tmp == min:
        if score < x:
            score = x
            res = idx + 1

print(avg, res)
