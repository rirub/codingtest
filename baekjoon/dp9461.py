T = int(input())
for _ in range(T):
    P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    n = int(input())
    if n <=10:
        print(P[n])
    else:
        for i in range(11,n+1):
            P.append(P[i-5]+P[i-1])
        print(P[n])