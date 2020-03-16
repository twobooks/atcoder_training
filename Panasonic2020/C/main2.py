from decimal import Decimal, getcontext
 
getcontext().prec = 1000
a,b,c = map(int,input().split())

ab = Decimal(a) * Decimal(b)
ab = ab.sqrt()

eps = Decimal(10) ** (-100)
 
cond = a + b + 2*ab < c
answer = 'Yes' if cond else 'No'
print(answer)