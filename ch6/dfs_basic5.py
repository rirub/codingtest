def dfs(w,sum, tsum):
# tum : 현재까지 판단한 무게
    global result
    if sum + (total-tsum) < result:
        return
    if sum>c:
        return
    if w == n: 
        if sum>result:
            result = sum
    else:
        dfs(w+1, sum+puppy[w], tsum+puppy[w])
        dfs(w+1, sum, tsum+puppy[w])


if __name__ == "__main__":
    c, n = map(int,input().split())
    puppy = []
    result = -2147000000
    for _ in range(n):
        puppy.append(int(input()))
    total = sum(puppy)
    dfs(0,0,0)
    print(result)