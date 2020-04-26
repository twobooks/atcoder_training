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
# arrA = np.array(input().split(),dtype=np.int64)
plusOrMinus = 0
num = arrA[0]
ans = 0
for i in range(N-1):
    if plusOrMinus == "+":
        if arrA[i]>arrA[i+1]:
            ans += 1
            plusOrMinus = 0
    elif plusOrMinus == "-":
        if arrA[i]<arrA[i+1]:
            ans += 1
            plusOrMinus = 0
    else:
        if arrA[i]<arrA[i+1]:
            plusOrMinus = "+"
        elif arrA[i]>arrA[i+1]:
            plusOrMinus = "-"
        else:
            pass

print(ans+1)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
