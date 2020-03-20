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
n,d = map(int,input().split())
arr = np.array([])
for _ in range(n):
    arr = np.append(arr,np.array(input().split(),dtype=np.int64))

arr = arr.reshape(n,-1)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        num = np.sqrt(sum((arr[i] - arr[j])**2))
        if num % 1 == 0:
            ans +=1
        else:
            continue

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

