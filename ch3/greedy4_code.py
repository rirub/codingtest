n, m =map(int,input().split())
w = list(map(int,input().split()))
w.sort()
cnt=0
i = 0
while w:
    if len(w)==1:
        cnt+=1
        break
    if w[0]+w[-1]>m:
        w.pop()
        cnt+=1
    else:
        w.pop(0)
        w.pop()
        cnt+=1
print(cnt)