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
n,m = map(int,input().split())
stair = [True for _ in range(n+1)]
for _ in range(m):
    broken = int(input())
    stair[broken] = False

mod = 1000000007

dp=[0 for _ in range(n+1)]

dp[0]=1
for now in range(n):
    for next in range(now+1,min(n,now+2)+1):
        if stair[next]:
            dp[next] += dp[now]
            dp[next] %= mod

print(dp[n])
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

