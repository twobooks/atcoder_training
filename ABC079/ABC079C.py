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
S = input()
A,B,C,D = map(int,list(S))
numlis = [B,C,D]

for bitlines in range(0,1<<3):
    ans = [A]
    num = A
    for target in range(3):
        if bitlines>>target & 1:
            num += numlis[target]
            ans = ans+["+",numlis[target]]
        else:
            num -= numlis[target]
            ans = ans+["-",numlis[target]]
    if num ==7:
        ans.append("=7")
        print(*ans,sep="")
        exit()

# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
