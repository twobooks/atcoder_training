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
N,T = map(int,input().split())
arrT = list(map(int,input().split()))

start = arrT[0]
end = 0
ans = 0
for i in range(N):
    if i == N-1:
        if arrT[i-1]+T>=arrT[i]:
            end = arrT[i]
            num = end-start+T
            ans += num
        else:
            ans += T
    elif arrT[i]+T>=arrT[i+1]:
        end = arrT[i]
        continue
    else:
        end = arrT[i]
        num = end-start+T
        ans += num
        start = arrT[i+1]

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
