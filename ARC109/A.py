A,B,X,Y = map(int,input().split())

if A<B:
    num1 = X + (B-A) * Y
    num2 = X + (B-A) * 2 * X
    print(min(num1,num2))
    exit()
elif A>B:
    num1 = X + (A-B-1) * Y
    num2 = X + (A-B-1) * 2 * X
    print(min(num1,num2))
    exit()
else:
    print(X)
    exit()