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
n,k = map(int,input().split())
# 配列入力の受け取り
arrP = list(map(int,input().split()))

sumlist = [0]
meansum = 0
for num in arrP:
    heikin = (1 + num)/2
    meansum += heikin
    sumlist.append(meansum)

ans = 0
for i in range(k,n+1):
    temp = sumlist[i] - sumlist[i-k]
    ans = max(ans,temp)

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

