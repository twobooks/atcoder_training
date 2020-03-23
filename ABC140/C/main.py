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
n = int(input())
arrB = list(map(int,input().split()))

arrA = [0 for _ in range(n)]

for i in range(len(arrB)):
    if i == 0:
        arrA[i] = arrB[i]
        arrA[i+1] = arrB[i]
    else:
        if arrB[i] <= arrA[i]:
            arrA[i] = arrB[i]
            arrA[i+1] = arrB[i]
        else:
            arrA[i+1] = arrB[i]

ans = sum(arrA)
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

