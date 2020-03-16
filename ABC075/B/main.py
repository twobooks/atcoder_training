# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import scipy as scp

# 盤面の受け取り
h,w = map(int,input().split())
board = [[] for _ in range(h)]
for i in range(h):
    board[i] = list(input())

moves = [(-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),(1,1)]
for ih in range(h):
    for iw in range(w):
        # print(ih,iw)
        if board[ih][iw] == "#":
            continue
        else:
            board[ih][iw] = 0
            for move in moves:
                mh = ih+move[0]
                mw = iw+move[1]
                if mh>=0 and mh<h and mw>=0 and mw<w:
                    if board[mh][mw] == "#":
                        board[ih][iw] += 1
                    else:
                        continue
                else:
                    continue
            continue

for row in board:
    print("".join(map(str,row)))

# print(ans)
# print("{:.10f}".format(ans))
