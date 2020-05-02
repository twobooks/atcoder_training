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
N = int(input())
arrA = list(map(int,input().split()))
travel1 = [abs(arrA[0])]
travel2 = [abs(arrA[1])]
for i in range(N-1):
    travel1.append(abs(arrA[i]-arrA[i+1]))
    if i <N-2:
        travel2.append(abs(arrA[i]-arrA[i+2])) 
    else:
        travel2.append(abs(arrA[i])) 
travel1.append(abs(arrA[N-1]))

sums = sum(travel1)

for i in range(N):
    print(sums-travel1[i]-travel1[i+1]+travel2[i])
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
