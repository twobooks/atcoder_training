# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
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
MOD = 10**9 + 7
N = int(input())
rows = [list(input()) for _ in range(5)]

def check(n):
    migi = 4*n-1
    if rows[1][migi-1]=="." and rows[2][migi-1]=="." and rows[3][migi-1]=="." and rows[4][migi-1]==".":
        return "7"
    elif rows[1][migi-1]=="." and rows[2][migi-1]=="." and rows[3][migi-1]==".":
        return "0"
    elif rows[0][migi-1]=="#" and rows[1][migi-1]=="#" and rows[2][migi-1]=="#":
        return "1"
    elif rows[0][migi-1]=="." and rows[1][migi-1]=="." and rows[2][migi-1]=="#":
        return "4"
    else:
        if rows[1][migi-2]=="#" and rows[1][migi]=="#" and rows[3][migi-2]=="#" and rows[3][migi]=="#":
            return "8"
        elif rows[1][migi-2]=="#" and rows[1][migi]=="." and rows[3][migi-2]=="#" and rows[3][migi]=="#":
            return "6"
        elif rows[1][migi-2]=="#" and rows[1][migi]=="#" and rows[3][migi-2]=="." and rows[3][migi]=="#":
            return "9"
        elif rows[1][migi-2]=="#" and rows[1][migi]=="." and rows[3][migi-2]=="." and rows[3][migi]=="#":
            return "5"
        elif rows[1][migi-2]=="." and rows[1][migi]=="#" and rows[3][migi-2]=="#" and rows[3][migi]==".":
            return "2"
        elif rows[1][migi-2]=="." and rows[1][migi]=="#" and rows[3][migi-2]=="." and rows[3][migi]=="#":
            return "3"
    
ans = ""
for i in range(1,N+1):
    char = check(i)
    ans += char

print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
