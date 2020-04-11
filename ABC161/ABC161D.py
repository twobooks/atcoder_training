# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
k = int(input())

que = deque(range(1,10)) 
for _ in range(k):
    tmp = que.popleft()
    if tmp % 10 !=0:
        val = tmp*10 + (tmp%10) - 1
        que.append(val)
    val = tmp*10 + (tmp%10)
    que.append(val)
    if tmp%10 != 9:
        val = tmp*10 + (tmp%10) + 1
        que.append(val)

ans = tmp
print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する