from _bisect import bisect_left
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    A.sort()
    B.sort()

    for x in A:
        sum+=bisect_left(B,x)
    print(sum)