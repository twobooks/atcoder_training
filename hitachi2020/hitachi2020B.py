# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
A,B,M = map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
times = M
table = []
for _ in range(times):
    x,y,c = list(map(int,input().split())) # 行列の場合
    table.append(arrA[x-1]+arrB[y-1]-c)

simplelow = min(arrA)+min(arrB)
ans = min(simplelow,min(table))

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
