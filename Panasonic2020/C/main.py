from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
a,b,c = map(int,input().split())

def check():
    if a+b >= c:
        return False
    if 4*a*b < (c-(a+b))**2:
        return True
    else:
        return False

if check():
    ans = "Yes"
else:
    ans = "No"
print(ans)
# print("{:.10f}".format(ans))
