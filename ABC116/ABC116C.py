# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())
arrA = list(map(int,input().split()))

#ゼロでリストを分割する
# def split_list(st):
#     lis = st.split("0")
#     lis = [l for l in lis if l != ""]
#     return lis

def split_list(lis,num=0):
    res = []
    tmp = []
    for i in lis:
        if i != num:
            tmp.append(i)
        elif i == num and len(tmp)>0:
            res.append(tmp)
            tmp = []
        else:
            continue
    else:
        res.append(tmp)
    res = [l for l in res if len(l) != 0]
    return res

stack = split_list(arrA)
ans = 0
#リスト毎に処理.len0は処理しない。
while len(stack)>0:
    lis1 = stack.pop()
    arr = np.array(list(map(int,list(lis1))))
    #最小値を引いたリストにする。最小値をansに加算
    nmin = min(arr)
    ans += nmin
    arr = arr - nmin
    s = list(arr)
    lis2 = split_list(s)
    stack = stack + lis2

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
