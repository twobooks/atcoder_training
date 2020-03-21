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

up2 = int(s[:2])
end2 = int(s[2:])

if (0<up2<13) and (0<end2<13):
    ans = "AMBIGUOUS"
elif 0<up2<13:
    ans = "MMYY"
elif 0<end2<13:
    ans = "YYMM"
else:
    ans = "NA"
# ans = YYMM, MMYY, AMBIGUOUS, NA
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

