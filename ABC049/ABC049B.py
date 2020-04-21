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
# 盤面の受け取り
H,W = map(int,input().split())
board = [[] for _ in range(H*2)]
for i in range(H):
    board[2*i] = list(input())
    board[2*i+1] = board[2*i].copy()

# print(*ans)   # unpackして出力。間にスペースが入る
for row in board:
    print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
