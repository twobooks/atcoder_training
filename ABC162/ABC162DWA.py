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

hikukazu = 0
for s in iter:
    for dot in range(2000):
        word = s[0] + "."*dot + s[1] + "."*dot + s[2]
        if len(word)>len(S):
            break
        hikukazu += len(re.findall(word,S))

ans = total - hikukazu
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
