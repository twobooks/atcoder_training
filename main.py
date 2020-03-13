# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
s = input()
n = int(input())
n,m = map(int,input().split())
# 配列入力の受け取り
arrA = list(map(int,input().split()))
arrA = np.array(input().split(),dtype=np.int64)
# 列ベクトルとかの受け取り
times = m
lists = []
for _ in range(times):
    lists += [input()]  #table.append(input())とも書ける
    # table.append(list(map(int,input().split()))) # 行列の場合
    # 整数として取り込むときは、 input() を int(input()) に置き換える。

strlist = "abcdefghijklmnopqrstuvwxyz"

print(ans)
print("{:.10f}".format(ans))
