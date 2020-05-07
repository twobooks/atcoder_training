# from math import factorial,sqrt,ceil,gcd,floor
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
A,B,N = map(int,input().split())

def yosiki(x):
    return floor(A*x/B)-A*floor(x/B)
if B == 1:
    print(0)
    exit()
elif A == B:
    x = min(N,B-1)
    print(yosiki(x))
    exit()
elif A>B:
    x = min(N,B-1)
    print(yosiki(x))
    exit()
elif A<B:
    x = min(N,B-1)
    print(yosiki(x))
    exit()
# print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
