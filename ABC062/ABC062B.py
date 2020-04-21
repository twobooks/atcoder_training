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
H,W = map(int,input().split())
# 盤面の受け取り
board = [[] for _ in range(H+2)]
board[0] = ["#"]*(W+2)
for i in range(1,H+1):
    board[i] = ["#"] + list(input()) + ["#"]
board[H+1] = ["#"]*(W+2)

for row in board:
    print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
