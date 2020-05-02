# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
S = input()
Slen = len(S)

if len(S)<=3:
    print(0)
    exit()

@lru_cache(maxsize=10000)
def check(n):
    if n%2019 == 0:
        return True
    else:
        return False

ans = 0
for i in range(Slen - 4 + 1):
    num_s = 4
    # for num_s in range(4,Slen+1-i):
    while num_s < Slen+1-i:
        num = int(S[i:i+num_s])
        if check(num):
            ans += 1
            num_s += 4
        else:
            num_s += 1
        # print(num,num_s,ans)

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
