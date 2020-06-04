# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
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

def primes(n):
    primes = []
    if n == 1:
        return primes
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            primes.append(i) 
    return primes

if N == 1:
    print(0)
    exit()

ans = 0
primenums = primes(N)
Zque = primenums.copy()
primenums = set(primenums)
Zset = set(Zque)
if len(Zque) == 0:
    print(1)
    exit()

Z = heappop(Zque)
while N >= Z:
    # print(N,Z)
    if N%Z == 0:
        ans += 1
        N = N//Z
    if Z in primenums:
        i = Z
        num = Z
        j = 2
        while num <= N:
            # print("num=",num,"N=",N,"j=",j)
            if not num in Zset:
                heappush(Zque,num)
                Zset.add(num)
            num = i**j
            j += 1
    if len(Zque)!=0:
        Z = heappop(Zque)
    else:
        break

print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
