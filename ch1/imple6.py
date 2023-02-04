N = int(input())
max = 0
result = 0
# a = list(map(int,input().split()))
a = map(int,input().split())
def digit_sum(x):
    num = 0
    tmp = str(x)
    for j in tmp:
        num += int(j)
    return num

for i in a:
    if max < digit_sum(i):
        result = i


print(result)
