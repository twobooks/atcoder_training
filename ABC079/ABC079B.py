# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
from functools import lru_cache # @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# slist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())

@lru_cache(maxsize=1000)
def lucas_number(n) -> int:
    if n<0:
        return -1
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas_number(n-1)+ lucas_number(n-2)

ans = lucas_number(N)

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
