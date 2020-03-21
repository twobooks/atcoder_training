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
n,x = map(int,input().split())
# 配列入力の受け取り
arrL = list(map(int,input().split()))

ans = [0]
junpzahyou = 0
i = 1
for i in arrL:
    junpzahyou += i
    if junpzahyou <= x:
        ans += [junpzahyou]
    else:
        continue

print(len(ans))
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

