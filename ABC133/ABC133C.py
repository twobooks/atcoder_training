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
l,r = map(int,input().split())

temp = 2019*2019
if r-l+1 >=2019:
    temp = 0
else:
    for i in range(l,r):
        for j in range(i+1,r+1):
            temp = min((i*j)%2019,temp)

ans = temp
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

