from math import factorial,sqrt
from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 列ベクトルとかの受け取り
times = n
lists = []
for _ in range(times):
    lists.append(list(map(int,input().split())))  #table.append(input())とも書ける

# print(lists)
routes = list(permus(range(0,n)))
# print(len(routes))
res = 0
for rout in routes:
    for i,town in enumerate(rout):
        if i == 0:
            continue
        else:
            xi = lists[rout[i]][0]
            yi = lists[rout[i]][1]
            xj = lists[rout[i-1]][0]
            yj = lists[rout[i-1]][1]
            res += sqrt((xi -xj)**2 + (yi-yj)**2)

ans = res/len(routes)

print("{:.10f}".format(ans))