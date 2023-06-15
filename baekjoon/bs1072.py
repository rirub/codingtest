import sys

def win_per(a,b):
    return (b/a)*100


if __name__=="__main__":
    x, y = map(int, input().split())
    mx = (x * x) // (101 * x - 100 * y)
    mn = 1
    z = win_per(x,y)
    result = 0
    if x==y:
        print(-1)
        sys.exit(0)
    else:
        while mn <= mx:
            mid = (mx+mn)//2
            if win_per(x+mid,y+mid)-z <1:
                mn = mid+1
            else:
                result = mid
                mx = mid-1

    print(result)
