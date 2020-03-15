# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
h,w = map(int,input().split())

if h==1 or w == 1:
    ans = 1
elif h%2 == 0:
    ans = h//2 * w
# elif w%2 ==0:
    # ans = w//2 * h
else:
    w1 = w//2
    w2 = w-w1
    ans = ((h//2)*w1) + (((h+1)//2)*(w2))
    
print(ans)
# print("{:.10f}".format(ans))
