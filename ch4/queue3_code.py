from collections import deque
need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        # 순서가 맞았다고 하더라도 yes 출력하면 안됨 dq가 남아있을 수 있음
        # 필수과목 다 안들었을 경우
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" % (i + 1))