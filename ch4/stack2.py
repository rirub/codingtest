a = list(input())
stack = []
cnt = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
    else:
        if a[i-1] != a[i]:
            cnt += len(stack)
        else:
            cnt += 1
        stack.pop()

print(cnt)


