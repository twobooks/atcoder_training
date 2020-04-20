# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N,K = map(int,input().split())

MOD = 10**9 + 7
ans = 0
lis = list(range(0,N+1))

for i in range(K,N+1+1):
    start = (i-1)*i//2
    end = N*i - start
    if end<=start:
        start,end = end,start
    num = end - start +1
    ans += num
ans %= MOD
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
