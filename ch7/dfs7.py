s, e = map(int,input().split())

tmp = e-s

cnt =0
if tmp>0:
    cnt += tmp//5
    tmp %= 5

    if tmp <=3:
        cnt += tmp
    elif tmp == 4:
        cnt += 2
    else:
        cnt += 1

else:
    cnt = -tmp
print(cnt)