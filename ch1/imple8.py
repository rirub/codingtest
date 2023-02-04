n = int(input())
a = list(map(int,input().split()))
def reverse(x):
    result = 0
    tmp = str(x)
    for i in range(len(tmp)-1,-1,-1):
        if(int(tmp[i])==0):
            continue
        else:
            result += int(tmp[i])*10**(i)
    return result

def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        return x

for i in range(n):
    reverseNum = reverse(a[i])
    result = isPrime(reverseNum)
    if  result != None:
        print(result, end=' ')