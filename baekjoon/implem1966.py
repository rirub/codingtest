from collections import deque
T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    queue = [(pos,val) for pos, val in enumerate(list(map(int,input().split())))]
    queue = deque(queue)
    cnt = 0
    target = queue[m]
    while queue:
        max_value = max(x[1] for x in queue)
        tmp = queue.popleft()
        if tmp[1] == max_value:
            cnt += 1
            if tmp == target:
                print(cnt)
                break
        else:
            queue.append(tmp)
