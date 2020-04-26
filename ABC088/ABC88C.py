# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N = 3
rows = [list(map(int,input().split())) for _ in range(N)]
arr = np.array(rows)

b1 = arr[0] -arr[0][0]
b2 = arr[1] -arr[1][0]
b3 = arr[2] -arr[2][0]
if not (list(b1)==list(b2)==list(b3)):
    print("No")
    exit()

arr = arr.T
a1 = arr[0]-arr[0][0]
a2 = arr[1]-arr[1][0]
a3 = arr[2]-arr[2][0]
if not(list(a1)==list(a2)==list(a3)):
    print("No")
    exit()

print("Yes")
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
