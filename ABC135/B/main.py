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
# 配列入力の受け取り
arrA = list(map(int,input().split()))
stdarr = list(range(1,n+1))

checknum = 0
for i in range(n):
    if arrA[i] != stdarr[i]:
        checknum += 1
    else:
        continue

if checknum <=2 and checknum!=1:
    ans = "YES"
else:
    ans = "NO"

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

