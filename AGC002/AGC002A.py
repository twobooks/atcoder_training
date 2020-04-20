# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# slist = "abcdefghijklmnopqrstuvwxyz"
a,b = map(int,input().split())

if a<0 and b<0:
    if (b-a)%2==0:
        ans = "Negative"
    else:
        ans = "Positive"
elif a<0 and b>=0:
    ans = "Zero"
elif a==0:
    ans = "Zero"
else:
    ans = "Positive"

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
