# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations,combinations,combinations_with_replacement
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
N,K = map(int,input().split())
lisA = [0] + list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)

if K<=N:
    i = K
    j = 1
    while i > 0:
        j = lisA[j]
        i -= 1
    print(j)
    exit()

checked = {1:0}
roopstnum = 0
i = 1
for n in range(1,N+2):
    if not lisA[i] in checked:
        checked[lisA[i]] = n
        i = lisA[i]
    else:
        roopstnum = lisA[i]
        roopstidx = checked[roopstnum]
        rooplen = n - roopstidx
        break

# print(roopstnum,rooplen,roopstidx,checked)
warukazu = rooplen
for k,v in checked.items():
    if (K-roopstidx) % warukazu == v - roopstidx:
        ans = k
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
