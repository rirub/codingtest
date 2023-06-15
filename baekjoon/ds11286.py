import sys
import heapq
input = sys.stdin.readline

a = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(a):
            print(heapq.heappop(a)[1])
        else:
            print(0)
    elif x < 0 :
       heapq.heappush(a,(-x,x))
    else:
        heapq.heappush(a,(x,x))
