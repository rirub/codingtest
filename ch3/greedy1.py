n = int(input())
time = []
res = 0
start=0
end=0
for _ in range(n):
    t = list(map(int,input().split()))
    time.append(t)
time.sort()
#이차원 배열 정렬 시 첫번째 원소 기준으로 정렬됨
for i in range(n):
    cnt = 1
    start = time[i][0]
    end = time[i][1]
    for j in range(i+1, n):
        if end<=time[j][0] and start<=time[j][0]:
            end = time[j][1]
            cnt +=1
    if cnt > res:
        res = cnt
print(res)