from collections import deque

n, m = map(int,input().split())
Q = [(pos,val) for pos, val in enumerate(list(map(int,input().split())))]

Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    # cur은 튜플 형태 !! (pos, val)
    # any 함수 : 단 하나라도 참이면 참
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0]==m:
            break
print(cnt)
