a = list(range(21))
for _ in range(10):
    x, y = map(int, input().split())
    for i in range((y-x+1)//2):
        a[x+i],a[y-i] = a[y-i],a[x+i]
a.pop(0)
for j in a:
    print(j, end=' ')

