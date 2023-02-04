a = int(input())
arr1 = list(map(int,input().split()))
b = int(input())
arr2 = list(map(int,input().split()))
result = []
i = 0
j = 0
for x in range(a+b):

    if (i < a) and (j < b):
        if(arr1[i]<arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    else:
        if i == a:
            result.append(arr2[j])
            j+=1
        elif j == b:
            result.append(arr1[i])
            i += 1



print(result)