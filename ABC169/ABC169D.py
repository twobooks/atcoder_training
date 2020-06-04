# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
from collections import deque,Counter
# from bisect import bisect_left
from heapq import heapify,heappush,heappop
# from numba import njit
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np    # numpy.lcm()
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

# slist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if N == 1:
    print(0)
    exit()

ans = 0
cnt_primes = Counter(prime_factorize(N))

for i in cnt_primes:
    j = 1
    while cnt_primes[i]>=0:
        cnt_primes[i] -= j
        if cnt_primes[i]>=0:
            ans += 1
        else:
            break
        j += 1

print(ans)