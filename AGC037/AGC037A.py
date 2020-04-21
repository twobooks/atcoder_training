# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
S = input()

i= 0
ans = 0
moji1 = ""
moji2 = ""
while i < len(S):
    if i == 0:
        moji1 = S[i]
        ans += 1
    else:
        moji2 = moji2 + S[i]
        if moji1 != moji2:
            ans += 1
            moji1 = moji2
            moji2 = ""
        else:
            moji2 = moji2 + S[i]
    i += 1

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
