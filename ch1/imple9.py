n = int(input())
a = []
result = []

for _ in range(n):
    a.append(list(map(int,input().split())))

for i in a:
    cnt = 0
    i.sort()
    if i[0]==i[1]:
        cnt +=1
        if i[0]==i[2]:
            cnt += 1
            result.append(10000+i[0]*1000)
        else:
            result.append(1000 + i[0] * 100)
    else:
        if i[1]==i[2]:
            result.append(1000 + i[1] * 100)
        else:
            result.append(i[2]*100)

print(max(result))