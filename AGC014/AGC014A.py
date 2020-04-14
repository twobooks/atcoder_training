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
A,B,C = map(int,input().split())
lis = [A,B,C]
lis.sort()

check = [lis]
ans = 0

while not(check[-1][0]%2==1 or check[-1][1]%2==1 or check[-1][2]%2==1):
    A,B,C = B//2 + C//2 , A//2 + C//2,B//2 + A//2
    temp = [A,B,C]
    temp.sort()
    if temp in check:
        print(-1)
        exit()
    check.append(temp)
    ans += 1

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
