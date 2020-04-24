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
board = [[] for _ in range(H)]
for i in range(H):
    board[i] = list(input())
moves = [(-1, 0), (0, -1), (0, 1),(1, 0)]

def check(h,w):
    for mh,mw in moves:
        x,y = h+mh,w+mw
        # print(x,y)
        if 0<=x<H and 0<=y<W and board[x][y]=="#":
            # print(board[x][y])
            return True
    return False
        
ans = "Yes"
for h in range(H):
    for w in range(W):
        if board[h][w]=="#":
            flg = check(h,w)
            if not flg:
                print("No")
                exit()

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
