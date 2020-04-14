# from math import factorial,sqrt,ceil
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
N,A,B = map(int,input().split())
S = input()

AplusB = A+B

ans = []
for i in range(len(S)):
    if S[i]=="a" and AplusB>0:
        ans.append("Yes")
        AplusB -= 1
    elif S[i]=="b" and AplusB>0 and B>0:
        ans.append("Yes")
        AplusB -= 1
        B -= 1
    else:
        ans.append("No")

print(*ans,sep="\n")
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
