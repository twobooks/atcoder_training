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
n = int(input())
# 列ベクトルとかの受け取り
lists = [int(input()) for _ in range(n)]

ans = 0
btn = 1
if not 2 in lists:
    ans = -1
else:
    while ans <=n:
        if lists[btn-1]==2:
            ans +=1
            break
        else:
            btn = lists[btn-1]
            ans +=1
            continue
    else:
        ans = -1

print(ans)
# print("{:.10f}".format(ans))
