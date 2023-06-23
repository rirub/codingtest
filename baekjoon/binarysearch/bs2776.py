import sys

T = int(input())
input = sys.stdin.readline

def binary_search(s,e,x):
    while s <= e:
        mid = (s + e) // 2
        if x == a_list[mid]:
            return 1
        elif x < a_list[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return 0

for _ in range(T):
    a = int(input())
    a_list = list(map(int,input().split()))
    b = int(input())
    b_list = list(map(int,input().split()))

    a_list.sort()

    for x in b_list:
        print(binary_search(0,a-1,x))

