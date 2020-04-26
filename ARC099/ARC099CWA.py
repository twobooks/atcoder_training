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
N,K = map(int,input().split())
arrA = list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)
if N==K:
    print(1)
    exit()

idx = arrA.index(1)
left = arrA[:idx]
right = arrA[idx+1:]

if arrA[0]==1 or arrA[-1]==1:
    if (N-1)%(K-1)==0:
        print((N-1)//(K-1))
        exit()
    else:
        print((N-1)//(K-1)+1)
        exit()

ans = 0
if len(left)+1<K:
    num = K-(len(left)+1)
    ans += 1
    left = []
    right = right[num:]
    print(right)
if len(right)+1<K:
    num = K-(len(right)+1)
    ans += 1
    right = []
    left = left[:-num] 
    print(left)

if len(left)%(K-1)==0:
    leftnum = len(left)//(K-1)
else:
    leftnum = len(left)//(K-1)+1
if len(right)%(K-1)==0:
    rightnum = len(right)//(K-1)
else:
    rightnum = len(right)//(K-1)+1
ans += leftnum + rightnum
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
