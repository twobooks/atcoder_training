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
# 列ベクトルとかの受け取り
dic = {}
for i in range(1,n+1):
    dic[i] = list(input().split())
    dic[i][1] = int(dic[i][1])

# print(dic)
ans = sorted(dic.items(),key=lambda x:(x[1][0],-x[1][1]))
# print(ans)

for i in range(len(ans)):
    print(ans[i][0])
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

