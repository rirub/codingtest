from collections import deque

n, k = map(int,input().split())
a = list(range(1,n+1))
print(a)
a = deque(a)


while len(a) !=1:
    for _ in range(k-1):
        a.append(a.popleft())
    a.popleft()

print(a[0])
