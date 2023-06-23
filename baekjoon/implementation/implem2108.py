N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
a.sort()
print(round(sum(a)/N))
print(a[N//2])

dic = dict()
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values())
mx_dict = []
for i in dic:
    if mx == dic[i]:
        mx_dict.append(i)
if len(mx_dict)>=2:
    print(mx_dict[1])
else:
    print(mx_dict[0])
print(max(a)-min(a))