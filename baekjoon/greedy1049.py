x = []
y = []
total = 0

n, m = map(int,input().split())
for _ in range(m):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
package_price = min(x)
one_price = min(y)

if package_price<one_price*6:
    total = (n//6)*package_price
    n %= 6
    if n*one_price < package_price:
        total += n * one_price
    else:
        total += package_price
else:
    total = n*one_price
print(total)

