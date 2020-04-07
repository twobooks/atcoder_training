# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
n,x,y = map(int,input().split())

ans = [0 for _ in range(n)]

for i in range(1,n):
    for j in range(i+1,n+1):
        kyori = min(j-i,abs(x-i)+1+abs(y-j),abs(i-y)+1+abs(x-j))
        ans[kyori] +=1

print(*ans[1:],sep="\n")
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する

