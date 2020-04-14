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
S = int(input())

lis = [0,S]

for i in range(2,1000000+1):
    if lis[i-1]%2==0:
        num = lis[i-1]//2
    if not lis[i-1]%2==0:
        num = 3*lis[i-1]+1
    if num in lis:
        ans = i
        break
    lis.append(num)

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
