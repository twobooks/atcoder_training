# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())

mod = 10**9 +7
ans = 1
for i in range(1,n+1):
    ans *= i
    ans = ans % mod

print(ans)