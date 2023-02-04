n = int(input())
a = list(map(int,input().split()))

res = []
check = [0]* n

for i in range(n):
    cnt = 0
    for j in range(n):
        if check[j]==0:
            cnt +=1
        if a[i]==cnt:
            break




