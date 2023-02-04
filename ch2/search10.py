a = [ list(map(int,input().split())) for _ in range(9) ]
def sdoku(a):
    for i in range(9):
        rows = [0] * (10)
        cols = [0] * (10)
        for j in range(9):
            if rows[a[i][j]] != 0 or cols[a[j][i]] !=0:
                return False
            else:
                rows[a[i][j]] += 1
                cols[a[j][i]] += 1
    else:
        for x in range(3):
            mini = [0] * (10)
            for y in range(3):
                for z in range(3):
                    if mini[a[x*3+y][x*3+z]] != 0:
                        return False
                    else:
                        mini[a[x * 3 + y][x * 3 + z]] += 1
        else:
            return True

if sdoku(a):
    print("YES")
else:
    print("NO")