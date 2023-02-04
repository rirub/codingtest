n = int(input())
res = []

def binary(n):
    if n//2 != 0:
        binary(n//2)
    else:
        if n%2 ==1:
            res.append(1)
        else:
            res.append(0)
binary(11)
print(res)