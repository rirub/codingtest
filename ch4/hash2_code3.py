a = input()
b = input()

# 알파벳 대소문자 총 52개
str1 = [0]*52
str2 = [0]*52

for x in a:
    # isupper 함수 : 대문자인지 확인
    # ord 함수 : 아스키 코드로 변환
    # 65~90 : A-Z , 97~120 : a-z
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1

for x in b:
    # isupper 함수 : 대문자인지 확인
    # ord 함수 : 아스키 코드로 변환
    # 65~90 : A-Z , 97~120 : a-z
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")