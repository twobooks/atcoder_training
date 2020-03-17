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
s = input()

lis = list(s)

ans = 0
for i in range(1,n):
    set1 = set(lis[0:i])
    set2 = set(lis[i:])
    checkset = set1 & set2
    ans = max(ans , len(checkset))

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

