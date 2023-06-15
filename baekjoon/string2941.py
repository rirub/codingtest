# eq = ['c','s','z']
# mi = ['c','d']
# word = input()
# cnt = len(word)
# for i in range(1,len(word)):
#     if word[i]=='=':
#         if word[i-1] in eq:
#             cnt -=1
#     elif word[i]=='-':
#         if word[i-1] in mi:
#             cnt -=1
#     elif word[i]=='j':
#         if word[i-1]=='n' or word[i-1]=='l':
#             cnt -=1
#     if i>=2:
#         if word[i-2:i+1]=="dz=":
#             cnt-=1
# print(cnt)
#

alias = ['c=','c-','dz=','d-','z=','lj','nj','s=']
b = input()
for i in alias:
    b = b.replace(i,'a')

print(len(b))