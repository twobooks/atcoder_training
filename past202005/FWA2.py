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

import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

N = int(input())
cnt = Counter()
for _ in range(N):
    tmp = Counter(input())
    for k,v in tmp.items():
        cnt[k] += v

div2combs = 0
mod2nums = 0
for k in cnt:
    div2combs += cnt[k]//2
    mod2nums += cnt[k]%2

# print(cnt,div2combs,mod2nums)
ans = deque()

if N == 1:
    for k in cnt:
        ans.append(k)
    print(*ans)
    exit()

if N%2 == 0:
    if div2combs >= N//2:
        for k,v in cnt.items():
            num = v
            if num//2>=1:
                while num >=2 and len(ans)<N:
                    ans.append(k)
                    ans.appendleft(k)
                    num -= 2
        print(*ans,sep="")
        exit()
    else:
        print(-1)
        exit()
else:
    if div2combs >= N//2 + 1:
        for k,v in cnt.items():
            num = v
            if num//2 >=1:
                if len(ans)==0 and num >=1:
                    ans.append(k)
                    num -= 1
                while len(ans)<N and num>=2:
                    ans.append(k)
                    ans.appendleft(k)
                    num -= 2
        print(*ans,sep="")
        exit()
    elif div2combs == N//2 and mod2nums >= 1:
        for k,v in cnt.items():
            num = v
            if num%2 ==1 and len(ans)==0:
                ans.append(k)
                cnt[k] -= 1
                break
        for k,v in cnt.items():
            num = v
            if num//2 >=1:
                while len(ans)<N and num>=2:
                    ans.append(k)
                    ans.appendleft(k)
                    num -= 2
        print(*ans,sep="")
        exit()
    else:
        print(-1)
        exit()

print(*ans,sep="")
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
