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

arrA = [0] + arrA
arrA.sort()

low,top = 0,len(arrA)+1

def check(i):
    if sum(arrA[:i]) <= x and i<=len(arrA):
        return True
    return False

while top - low>1:
    half = (top+low)//2
    if check(half):
        low = half
    else:
        top = half

if sum(arrA[:low])==x:
    ans = low
else:
    ans = low-1
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
