from collections import deque
a = []
while True:
    n = int(input())
    if n==-1:
        break
    elif n==0:
        if a:
            tmp = a.pop()
            print(tmp)
        else:
            print(-1)
    else:
        a.append(n)
        a.sort(reverse=True)