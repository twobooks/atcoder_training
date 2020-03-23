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
n,m = map(int,input().split())
# 列ベクトルとかの受け取り
lists = [list(map(int,input().split())) for _ in range(m)]

maxL = 1
minR = n
for i in range(m):
    maxL = max(maxL,lists[i][0])
    minR = min(minR,lists[i][1])

ans = minR - maxL +1
if ans <= 0:
    ans = 0

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

