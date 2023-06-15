n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

print(min(a))
print(max(a))