# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
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
X = int(input())

dp = {100:1,101:1,102:1,103:1,104:1,105:1}
lis = [100,101,102,103,104,105]
que = deque([100,101,102,103,104,105])
while len(que)>0:
    num = que.popleft()
    for i in lis:
        dp[num+i] = 1
        if num+i <= 100000 and not(num+i in que):
            que.append(num + i)

if X in dp:
    ans = 1
else:
    ans = 0

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
