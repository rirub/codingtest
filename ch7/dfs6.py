def DFS(L,p):
    global cnt
    if L==len(code):
        print(res)
        cnt += 1
    else:
        for i in range(1,26):
            if code[L]==i:
                res.append(i)
                DFS(L+1,p+1)
            else:
                if L< len(code)-1 and code[L]*10+code[L+1]==i:
                    res.append(i)
                    DFS(L + 2, p + 1)
if __name__=="__main__":
    code = list(map(int,input().split()))
    res = []
    cnt = 0
    a = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']

    DFS(0,0)
    print(cnt)
