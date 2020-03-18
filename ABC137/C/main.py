# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 列ベクトルとかの受け取り
lists = ["".join(sorted(list(input()))) for _ in range(n)]

strcount = Counter(lists)

ans = 0
for i,n in strcount.items():
    if n == 1:
        continue
    else:
        ans += n*(n-1)//2

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

