# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations,combinations,combinations_with_replacement
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
N,M,X = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(N)]
rows = np.array(rows)

ans = 10**5 * N +1
for bitlines in range(0,1<<N):
    tmp = np.array([0]*(M+1))
    for target in range(N):
        if bitlines>>target & 1:
            tmp = tmp + rows[target]
        else:
            continue
    if np.bincount((tmp>=X)[1:],minlength=2)[1]==M:
        ans = min(ans,tmp[0])

if ans == 10**5 * N +1:
    ans = -1

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
