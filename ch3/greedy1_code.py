n = int(input())
meeting = []
for i in range(n):
    s, e = map(int,input().split())
    meeting.append((s,e))
    # 튜플 형태로 들어옴
    meeting.sort(key=lambda x : (x[1],x[0]))
    # 매개변수를 두개 둬서 종료 시간이 같으면 먼저 시작하는게 더 우선순위 높게 정렬
et = 0
cnt = 0
for s, e in meeting:
    if s>=et:
        et = e
        cnt += 1
print(cnt)