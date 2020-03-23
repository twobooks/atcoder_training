# from math import factorial,sqrt
# from itertools import permutations as permus
from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# 入力の受け取り
a,b,c,d = map(int,input().split())

def lcm(x:int, y:int)->int:
    """
    return Least common multiple (最小公倍数)
    """
    return (x * y) // gcd(x, y)

e = lcm(c,d)

if c == 1 or d ==1:
    ans = 0
else:
    ans = b-a+1
    minus1 = b//c - (a-1)//c
    minus2 = b//d - (a-1)//d
    plus = b//e - (a-1)//e
    ans = ans -minus1 -minus2 +plus

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

