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
rows = [list(map(int,input().split())) for _ in range(N)]

pos = [0,0]
time = 0
for row in rows:
    t,x,y = row
    tt = t - time
    xx = abs(x-pos[0])
    yy = abs(y-pos[1])
    num = tt-(xx+yy)
    if num>=0 and num%2==0:
        pos = [x,y]
        time = t
    else:
        print("No")
        exit()

print("Yes")
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
