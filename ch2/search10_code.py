a = [ list(map(int,input().split())) for _ in range(9) ]
def check(a):
    for i in range(9):
        rows = [0] * (10)
        cols = [0] * (10)
        for j in range(9):
            rows[a[i][j]] = 1
            cols[a[i][j]] = 1
        if sum(rows)!=9 or sum(cols)!=9:
            return False
    for x in range(3):
        mini = [0] * (10)
        for y in range(3):
            for z in range(3):
                mini[a[x*3+y][x*3+z]] = 1

            if sum(mini)!=9:
                return False
    return True



if check(a):
    print("YES")
else:
    print("NO")