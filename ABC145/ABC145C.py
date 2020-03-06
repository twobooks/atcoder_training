a,b,x = map(int,input().split())

def daikin(n):
    retu = a*n + b*len(str(n))
    # print(retu)
    return retu

num = x//a
keta = len(str(num))
if num == 0:
    print(0)
elif b > x:
    print(0)
elif x>=daikin(10**9):
    print(10**9)
else:
    top = x
    bottom = 0
    while top - bottom > 1: 
        harf = (top+bottom)//2
        if daikin(harf)<=x:
            bottom=harf
        else:
            top=harf
    print(bottom)
    # for i in range(num,0,-1):
    #     if daikin(i) <= x:
    #         ans = i
    #         print(ans)
    #         break
