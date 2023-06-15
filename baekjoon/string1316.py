n = int(input())
cnt = n
for _ in range(n):
    word = input()
    for i in range(1,len(word)):
        if word[i]==word[i-1]:
            pass
        elif word[i-1] in word[i+1:]:
            cnt -=1
            break

print(cnt)