x = dict()
y = dict()

a = input()
b = input()

for i in range(len(a)):
    tmp = a[i]
    if tmp in x:
        x[tmp]+=1
    else:
        x[tmp] = 1

for i in range(len(b)):
    tmp = b[i]
    if tmp in y:
        y[tmp]+=1
    else:
        y[tmp]=1
if len(x)!=len(y):
    print("NO")
else:
    for key, val in x.items():
        if y[key]!=val:
            print("NO")
            break
    else:
        print("YES")