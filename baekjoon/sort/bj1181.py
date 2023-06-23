import sys

input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    word = input()
    a.append((len(word),word))
    a = set(a)
b = sorted(a, key=lambda a: (a[0],a[1]))

for x in b:
    print(x[1],end='')