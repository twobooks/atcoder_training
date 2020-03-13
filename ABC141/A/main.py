# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
s = input()

lis = ["Sunny","Cloudy","Rainy"]

idx = (lis.index(s) +1) % 3
ans = lis[idx]

print(ans)