# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
# from collections import Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n,k = map(int,input().split())
# 配列入力の受け取り
arrh = np.array(input().split(),dtype=np.int64)

filter = arrh >= k
ans = len(arrh[filter])

print(ans)