a,k = map(int,input().split())

ch = [0] * (k+1)
ch[a+1]=1
ch[a*2]=1
for i in range(a+1,k):
    if i+1<=k:
        if ch[i + 1] == 0:
            ch[i+1]=ch[i]+1
        else:
            ch[i+1]=min(ch[i+1],ch[i]+1)
    if i*2<=k:
        if ch[i*2]==0:
            ch[i*2] = ch[i]+1
        else:
            ch[i*2] = min(ch[i*2], ch[i] + 1)
    else:
        continue

print(ch[k])