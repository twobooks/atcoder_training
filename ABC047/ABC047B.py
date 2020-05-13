W,H,N = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(N)]

Xleft = 0
Xright = W
Ylow = 0
Yhigh = H
for X,Y,A in rows:
    if A == 1:
        Xleft = max(X,Xleft)
    elif A == 2:
        Xright = min(X,Xright)
    elif A == 3:
        Ylow = max(Y,Ylow)
    else:
        Yhigh = min(Y,Yhigh)

ans = max(Yhigh-Ylow,0) * max(Xright-Xleft,0)
print(ans)