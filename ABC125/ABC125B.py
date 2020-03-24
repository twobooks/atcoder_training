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
# 配列入力の受け取り
arrV = np.array(input().split(),dtype=np.int64)
arrC = np.array(input().split(),dtype=np.int64)

arrA = arrV - arrC

filter = arrA > 0
ans = sum(arrA[filter])

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

