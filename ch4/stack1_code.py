num, m = map(int,input().split())
num = list(map(int,str(num)))

stack = []

for x in num:
    while stack and m>0 and x>stack[-1]:
        m-=1
        stack.pop()
    stack.append(x)

if m!=0:
    stack = stack[:-m]
res = ''.join(map(str,stack))
print(res)