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
arrA = list(map(int,input().split()))

cbdp = [0,0]
cbdp2 = [i*(i-1)//2 for i in range(2,n+1)]
cbdp += cbdp2
# print(cbdp)

ctA = Counter(arrA)
# print(ctA)

totalconb = 0
for v in ctA.values():
    totalconb += cbdp[v]
# print(totalconb)

for a in arrA:
    print(totalconb-cbdp[ctA[a]]+cbdp[ctA[a]-1])

# print(*ans,sep="\n")
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

