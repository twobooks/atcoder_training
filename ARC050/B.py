R,B = list(map(int,input().split()))
x,y = list(map(int,input().split()))

def check(X):
    r = R-X
    b = B-X
    if r<0 or b<0:
        return False
    num = r//(x-1) + b//(y-1)
    return (num>=X)

ok = 0
ng = 10**18+1
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

if ok ==0:
    print(0)
else:
    print(ok)