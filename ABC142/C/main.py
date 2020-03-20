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

ans = [0 for _ in range(n)]
for i,v in enumerate(arrA):
    ans[v-1] = i+1

print(*ans)