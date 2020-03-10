# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque

# import numpy as np
# import scipy as scp

# 入力の受け取り
d,n = map(int,input().split())
if d ==0:
    if n <=99:
        ans = n
    elif n==100:
        ans = 101
elif d == 1:
    if n <=99:
        ans = n*100
    elif n==100:
        ans = 101*100
else:
    if n <=99:
        ans = n*100**2
    elif n==100:
        ans = 101*100**2

print(ans)