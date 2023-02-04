from collections import deque

subject = list(input())
n = int(input())
subject = deque(subject)
print(subject[0])

for i in range(n):
    a = list(input())
    tmp = subject
    for x in a:
        if x in tmp:
            if x == tmp[0]:
                tmp.popleft()
            else:
                print(i+1,"NO")
                break
    else:
        print(i+1,"YES")


