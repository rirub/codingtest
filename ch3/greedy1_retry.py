n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1],x[0]))

start = 0
end = 0
cnt = 0
for s,e in meeting:
    if s>=end:
        end = e
        cnt += 1
print(cnt)