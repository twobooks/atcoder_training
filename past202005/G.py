# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
from collections import deque,Counter
# from bisect import bisect_left
# from heapq import heappush,heappop
# from numba import njit
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

# slist = "abcdefghijklmnopqrstuvwxyz"
N,X,Y = map(int,input().split())
board = [["."]*403 for _ in range(403)]
board[201][201] = "S"
board[X+201][Y+201] = "G"
for _ in range(N):
    x,y = map(int,input().split())
    board[x+201][y+201] = "#"

moves = [(1, 1),(0, 1), (-1, 1), (1, 0), (-1, 0),(0,-1)]
que = deque([(201,201)])
checked = {(201,201):0}
def bfs(board,que,moves,checked):
    while len(que) > 0:
        now = que.popleft()
        num = checked[now] + 1
        for xnum,ynum in moves:
            x = now[0] + xnum
            y = now[1] + ynum
            if x<0 or x>402 or y<0 or y>402:
                continue
            next_point = (x,y)
            if board[x][y] == "#":
                continue
            if next_point in checked:
                continue
            que.append(next_point)
            checked[next_point] = num
            if board[x][y] == "G":
                return checked[next_point]

ans = bfs(board,que,moves,checked)
print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
