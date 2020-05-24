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

slist = "abcdefghijklmnopqrstuvwxyz" #26文字。idxは25まで
arrS = np.zeros(26).astype("int64")
N = int(input())
for _ in range(N):
    cnt = Counter(input())
    for k,v in cnt.items():
        arrS[ord(k)-97] += v

ans = deque()

if N == 1:
    for i in range(26):
        if arrS[i] >=1:
            ans.append(chr(i+97))
    print(*ans)
    exit()

if N%2 == 0:
    if sum(arrS//2) >= N//2:
        for i in range(26):
            if arrS[i]//2 >=1:
                num = arrS[i]
                while len(ans)<N and num>=2:
                    ans.appendleft(chr(i+97))
                    ans.append(chr(i+97))
                    num-=2
    else:
        print(-1)
        exit()
else:
    if sum(arrS//2) >= N//2 + 1:
        for i in range(26):
            if arrS[i]//2 >=1:
                num = arrS[i]
                if len(ans)==0 and num >=1:
                    ans.append(chr(i+97))
                    num -= 1
                while len(ans)<N and num>=2:
                    ans.appendleft(chr(i+97))
                    ans.append(chr(i+97))
                    num-=2
        print(*ans,sep="")
        exit()
    elif sum(arrS//2) == N//2 and sum(arrS%2) >= 1:
        for i in range(26):
            if arrS[i]%2 ==1 and len(ans)==0:
                ans.append(chr(i+97))
        for i in range(26):
            if arrS[i]//2 >=1:
                num = arrS[i]
                while len(ans)<N and num>=2:
                    ans.appendleft(chr(i+97))
                    ans.append(chr(i+97))
                    num-=2
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
