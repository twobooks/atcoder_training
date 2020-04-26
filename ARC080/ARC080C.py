# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())
arrA = list(map(int,input().split()))
arrA = np.array(arrA)

arrA = arrA % 4
num4s = len(arrA[arrA==0])
num2s = len(arrA[arrA==2])
num13s = len(arrA) - num2s - num4s

if num13s - num4s == 0:
    ans = "Yes"
elif num13s - num4s == 1 and num2s>0:
    ans = "No"
elif num13s - num4s > 1:
    ans = "No"
else:
    ans = "Yes"
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
