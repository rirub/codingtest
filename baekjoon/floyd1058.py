n = int(input())
a = []
result = [0]*n
for _ in range(n):
    tmp = list(input())
    a.append(tmp)

for i in range(n):
    for j in range(n):
        if a[i][j]=='Y':
            result[i]+=1
        else:
            if i!=j:
                for k in range(n):
                    if i!=k and k!=j:
                        if a[i][k]=='Y'and a[k][j]=='Y':
                            result[i]+=1
print(max(result))