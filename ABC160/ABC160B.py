# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# strlist = "abcdefghijklmnopqrstuvwxyz"
x = int(input())

jpy500 = 0
jpy5 = 0

jpy500 = x//500
x -= 500*jpy500
jpy5 = x//5

ans = jpy500*1000 + jpy5*5
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

