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
arrP = list(map(int,input().split()))

ans = 0
for i in range(1,n-1):
    if arrP[i-1]<arrP[i]<arrP[i+1] or arrP[i-1]>arrP[i]>arrP[i+1]:
        ans += 1

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

