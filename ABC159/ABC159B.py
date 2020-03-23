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
revs = s[::-1]
n = len(s)
s2 = s[:(n-1)//2]
revs2 = s2[::-1]
s3 = s[(n+3)//2-1:]
revs3 = s3[::-1]

# print(s == revs)
# print(s2 == revs2)
# print(s3 == revs3)
if s == revs and s2 == revs2 and s3 == revs3:
    ans = "Yes"
else:
    ans = "No"

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

