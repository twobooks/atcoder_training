# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrD = np.array(input().split(),dtype=np.int64)

AA,BB = np.meshgrid(arrD,arrD)
a = np.dot(AA.flatten(),BB.flatten())
# print(a)
b = sum(arrD**2)
# print(b)

ans = (a-b)//2

print(ans)