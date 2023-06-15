from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline()
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()
res = []

for x in b:
    res.append(bisect_right(a, x) - bisect_left(a, x))
for x in res:
    print(x,end=' ')
