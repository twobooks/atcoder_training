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
N,x = map(int,input().split())
arrA = list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)

arrA.sort()
ans = 0
flg = True
for i in range(N):
    if arrA[i]<=x:
        x -= arrA[i]
        ans += 1
    else:
        flg = False

# print(flg,x)
if flg and x>0:
    print(ans-1)
elif flg and x == 0:
    print(ans)
elif not flg and x==0:
    print(ans)
else:
    print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
