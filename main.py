# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
# from collections import Counter

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
query_list = []
for _ in range(times):
    query_list += [input()]  #table.append(input())とも書ける
    # table.append(list(map(int,input().split()))) # 行列の場合
    # 整数として取り込むときは、 input() を int(input()) に置き換える。

strlist = "abcdefghijklmnopqrstuvwxyz"

print(ans)