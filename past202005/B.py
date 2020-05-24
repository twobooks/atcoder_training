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
N,M,Q = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(Q)]

# problem_scores = N - SeikaiNum <=変化する
problem_scores = [0] + [N] * M
# people_score = sum(problem_score)
people_answers = {}

for i in range(Q):
    if rows[i][0] == 2:
        idx1 = rows[i][1]
        problem_num = rows[i][2]
        if not idx1 in people_answers:
            people_answers[idx1] = [rows[i][2]]
            problem_scores[problem_num] -= 1
        else:
            people_answers[idx1] += [rows[i][2]]
            problem_scores[problem_num] -= 1
    else:
        idx2 = rows[i][1]
        if not idx2 in people_answers:
            print(0)
            continue
        persons_score = 0
        for j in people_answers[idx2]:
            persons_score += problem_scores[j]
        print(persons_score)