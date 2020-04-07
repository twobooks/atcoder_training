# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# strlist = "abcdefghijklmnopqrstuvwxyz"
k,n = map(int,input().split())
# 配列入力の受け取り
arrA = list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)

ans = k+10
for i in range(n):
    if i == 0:
        migi = arrA[n-1]-arrA[0]
        hidari = k - (arrA[1]-arrA[0])
        ans = min(migi,hidari,ans)
    elif i == n-1:
        migi = k -(arrA[n-1] - arrA[n-2])
        hidari = arrA[n-1]-arrA[0]
        ans = min(migi,hidari,ans)
    else:
        migi = arrA[i-1] + k-arrA[i]
        hidari = k-(arrA[i+1]-arrA[i])
        ans = min(migi,hidari,ans)

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

