n = int(input())

def check(a):
    a = a.lower()
    n = len(a)
    for i in range (n//2):
        if a[i] == a[n-1-i]:
            continue
        else:
            return False
    else:
        return True


for i in range(1,n+1):
    a = input()
    result = check(a)
    if result == True:
        print("YES")
    else:
        print("NO")


