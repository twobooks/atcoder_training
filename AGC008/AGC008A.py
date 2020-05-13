X,Y = map(int,input().split())

sa = abs(abs(X)-abs(Y))

if Y>X>0:
    print(sa)
    exit()
elif X>Y>0:
    print(sa+2)
    exit()
elif Y<X<0:
    print(sa + 2)
    exit()
elif X<Y<0:
    print(sa)
    exit()
elif X>0 and Y<0:
    print(sa + 1)
    exit()
elif X<0 and Y>0:
    print(sa + 1)
    exit()
elif X == 0:
    if Y>0:
        print(sa)
        exit()
    else:
        print(sa+1)
        exit()
elif Y == 0:
    if X>0:
        print(sa+1)
        exit()
    else:
        print(sa)
        exit()








