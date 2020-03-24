# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import scipy as scp

# 入力の受け取り
n,m = map(int,input().split())
# 配列入力の受け取り
lights = [list(map(int,input().split())) for _ in range(m)]
lightflg = list(map(int,input().split()))

ans = 0
for switch_bits in range(0,1<<n):
    allflg = True
    for i in range(m):
        flg = lightflg[i]
        on_count = 0
        for switch in lights[i][1:]:
            switch -= 1
            if switch_bits>>switch & 1:
                on_count += 1
        if on_count%2 != flg:
            allflg = False
            break
    if allflg:
        ans += 1

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
