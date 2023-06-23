n = list(input())
n = list(map(int,n))
n.sort(reverse=True)

if n[-1] != 0:
    print(-1)
else:
    if sum(n)%3 ==0:
        for x in n:
            print(x,end='')
    else:
        print(-1)