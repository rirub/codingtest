n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)

cnt =0
mx = 0

for i in a:
    cnt +=1
    if mx < i*cnt:
        mx = i*cnt
print(mx)