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
A,B,C = map(int,input().split())
lis = [A,B,C]
lis.sort()
cnt_1 = lis[2]-lis[1]
nokori = lis[2]-lis[0]-cnt_1
if (lis[2]-lis[0]-cnt_1)%2 == 0:
    cnt_2 = nokori//2
else:
    cnt_2 = (nokori+1)//2 + 1

ans = cnt_1+cnt_2
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
