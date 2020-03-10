# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrA = np.array(input().split(),dtype=np.int64)

ans = sum(arrA -1)

print(ans)