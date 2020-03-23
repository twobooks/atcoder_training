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
h,w,k = map(int,input().split())
# 盤面の受け取り
board = [[] for _ in range(h)]
for i in range(h):
    board[i] = list(input())

choko = np.array(board,dtype="int64")


print(choko)

ans = 0
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

