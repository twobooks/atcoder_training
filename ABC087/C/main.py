# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrA1 = np.array(input().split(),dtype=np.int64)
arrA2 = np.array(input().split(),dtype=np.int64)

ans = 0
for i in range(1,n+1):
    res = sum(arrA1[0:i])+sum(arrA2[i-1:n])
    ans = max(ans,res)

print(ans)