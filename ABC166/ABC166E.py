# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations,combinations,combinations_with_replacement
from collections import deque,Counter
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
N = int(input())
lisA = [0] + list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)
# j-i == Ai+Aj => i+Ai == j-Aj
lisI = []
for i,num in enumerate(lisA):
    lisI.append(i+num)

cnt = Counter(lisI[1:])
ans = 0
for j,num in enumerate(lisA):
    if j == 0:
        continue
    elif j-num in cnt:
        ans += cnt[j-num]
    else:
        continue

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
