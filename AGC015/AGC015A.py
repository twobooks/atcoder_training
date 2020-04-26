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
N,A,B = map(int,input().split())

if N == 0:
    print(0)
    exit()
elif N == 1 and A==B:
    print(1)
    exit()
elif N == 1 and A!=B:
    print(0)
    exit()
elif A>B:
    print(0)
    exit()
elif N==2:
    print(1)
    exit()
else:
    n = N-2
    ans = B*n - A*n +1
    print(ans)
    exit()
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
