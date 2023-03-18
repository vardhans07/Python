def findGcd(x, y):
    if x==0:
        return y
    elif y==0:
        return x
    else:
        a = max(x,y)
        b = min(x,y)
        r = a % b
        return findGcd(b, r)
x=int(input())
y=int(input())

findGcd(x, y)
