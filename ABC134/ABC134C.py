# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 列ベクトルとかの受け取り
lists = [int(input()) for _ in range(n)]
arr = np.array(lists)

maxnum = max(lists)
filter = arr == maxnum
maxarr = arr[filter]
filt2 = arr < maxnum
nextmaxnum = max(arr[filt2]) if len(arr[filt2])!=0 else maxnum

if len(maxarr)>1:
    for _ in range(n):
        print(maxnum)
else:
    for num in arr:
        if num != maxnum:
            print(maxnum)
        else:
            print(nextmaxnum)