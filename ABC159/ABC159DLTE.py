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

ctA = Counter(arrA)
dp = {}
cbdp = {}
for i in range(len(arrA)):
    if arrA[i] in dp:
        print(dp[arrA[i]])
        continue
    ctA[arrA[i]] -= 1
    temp = 0
    for v in ctA.values():
        if v<=1:
            continue
        elif v in cbdp:
            temp += cbdp[v]
        else:
            temp += v*(v-1)//2
            cbdp[v] = v*(v-1)//2
    print(temp)
    dp[i] = temp
    ctA[i] += 1

# print(*ans,sep="\n")
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

