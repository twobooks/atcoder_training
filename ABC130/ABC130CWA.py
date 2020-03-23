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
W,H,x,y = map(int,input().split())

surface = W * H
ans = [0,0]
# x,yが周上なら最大値は半分で他の分け方は無い
if not(0<x<W and 0<y<H):
    ans = [surface/2,0]
# 点が中央の場合
elif x==W/2 and y==H/2:
    ans = [surface/2,1]
# 点が対角線上の場合（中央除く）
# 対角線の判定はW:H=x:y->H*x==W*y or Wy=HW-Hxをx,yが満たす場合
elif H*x==W*y or W*y == H*W-H*x:
    ans = [surface/2,0]
# x,yが内部なら最大値はmax(min(H*x,総面積-H*x),min(W*y,総面積-W*y))
# もし一致するなら分け方複数ある
else:
    xx = min(H*x,surface-H*x)
    yy = min(W*y,surface-W*y)
    ans[0] = max(xx,yy)
    ans[1] = 1 if xx==yy else 0

print(*ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

