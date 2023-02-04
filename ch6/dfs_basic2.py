def dfs(x):
    if x>7:
        return
    else:
        dfs(x*2)
        print(x, end=' ')
        dfs(x*2+1)


if __name__== "__main__":
    dfs(1)