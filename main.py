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
n = int(input())
n,m = map(int,input().split())
# 配列入力の受け取り
arrA = list(map(int,input().split()))
arrA = np.array(input().split(),dtype=np.int64)
# 列ベクトルとかの受け取り
lists = [int(input()) for _ in range(n)]
# times = m
# lists = []
# for _ in range(times):
#     lists += [input()]  #table.append(input())とも書ける
#     # table.append(list(map(int,input().split()))) # 行列の場合

# 盤面の受け取り
h,w = map(int,input().split())
board = [[] for _ in range(h)]
for i in range(h):
    board[i] = list(input())
moves = [(-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),(1,1)]

strlist = "abcdefghijklmnopqrstuvwxyz"

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

