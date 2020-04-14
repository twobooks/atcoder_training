# from math import factorial,sqrt,ceil
from itertools import permutations as permus
# from fractions import gcd
from collections import deque,Counter
import re
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())
S = input()

Sset = Counter(S)
iter = permus(list("RGB")) 

total = Sset["R"]*Sset["G"]*Sset["B"]

Slen = len(S)
hikukazu = 0
for i in range(Slen):
    for num in range(1,Slen//2+1):
        j = i+num
        k = i+num*2
        if k>Slen-1:
            break
        if S[i]!=S[j] and S[i]!=S[k] and S[k]!=S[j]:
            hikukazu += 1

ans = total - hikukazu
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
