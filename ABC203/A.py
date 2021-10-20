a,b,c = list(map(int,input().split()))

if a == b:
    print(c)
    exit()
elif c==a:
    print(b)
    exit()
elif c==b:
    print(a)
    exit()
else:
    print(0)