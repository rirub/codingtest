n, m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in range(n):
    tmp = a[i]
    if a[i] == m:
        cnt += 1
        continue
    for j in range(i+1,n):
        tmp += a[j]
        if(tmp == m):
            cnt+=1
            continue
        elif(tmp > m):
            break
print(cnt)