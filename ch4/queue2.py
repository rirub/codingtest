from collections import deque

n, m = map(int,input().split())
a = list(map(int,input().split()))
a = deque(a)
target = a[m]
cnt = 0
while True:
    if max(a) == a[0] and max(a)==target:
        cnt += 1
        break
    if max(a)==a[0]:
        cnt +=1
        a.popleft()
    else:
        tmp = a[0]
        a.popleft()
        a.append(tmp)

print(cnt)
