# import math
# from itertools import permutations as permus
# from fractions import gcd

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
n,m = map(int,input().split())
# 配列入力の受け取り
arrA = list(map(int,input().split()))
arrA = np.array(input().split(),dtype=np.int64)
# 列ベクトルとかの受け取り
times = m
table = []
for _ in range(times):
    table.append(input())  # S += [input()] とも書ける
    # table.append(list(input().split())) # 行列の場合
    # 整数として取り込むときは、 input() を int(input()) に置き換える。

strlist = "abcdefghijklmnopqrstuvwxyz"

print(ans)