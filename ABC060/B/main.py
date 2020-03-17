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
a,b,c = map(int,input().split())

checklis = []
i = a
while not i in checklis:
    num = i % b
    if num == c:
        ans = "YES"
        break
    else:
        checklis.append(num)
        if num==0:
            checklis.append(i)
        i = num + a
else:
    ans = "NO"

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

