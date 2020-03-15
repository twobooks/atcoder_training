# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# 入力の受け取り
s = input()

slis = list(s)
slis = slis[:-1]

ans = len(s)

while len(slis) > 0:
    if len(slis)%2 == 1:
        slis = slis[:-1]
        continue
    else:
        slicenum = len(slis)//2
        if slis[:slicenum] == slis[slicenum:]:
            ans = len(slis)
            break
        else:
            slis =slis[:-1]
            continue
    
print(ans)
# print("{:.10f}".format(ans))
