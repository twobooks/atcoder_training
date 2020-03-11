# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
# from collections import Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrA = np.array(input().split(),dtype=np.int64)

ans = 0
while len(arrA)>0:
    filter = (arrA%2 == 0)
    ans += len(arrA[filter])
    arrA = arrA[filter]//2

print(ans)