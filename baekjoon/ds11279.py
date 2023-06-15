import heapq

n = int(input())
a = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(a)==0:
            print(0)
        else:
            print(-1*heapq.heappop(a))

    else:
        heapq.heappush(a,-x)
