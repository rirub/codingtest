a = list(input())
result1 = []
result2 = 0
cnt = 0
for i in range(len(a)):
    a[i] = ord(a[i])

for i in a:
    if i>=48 and i<=57:
        result1.append(int(chr(i)))
lenA = len(result1)
for j in range(1,lenA+1):
    result2 += result1[j-1] * (10**(lenA-j))
print(result2)

for k in range(1, result2+1):
    if result2%k == 0:
        cnt+=1




print(cnt)