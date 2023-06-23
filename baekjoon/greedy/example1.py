s = input()
result = 1
for i in range(len(s)):
    num = int(s[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= int(s[i])
print(result)