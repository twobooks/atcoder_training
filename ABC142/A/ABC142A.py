# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
# from collections import Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())

if n%2 == 0:
    ans = 0.5
elif n==1:
    ans = 1.0
else:
    ans = (n+1)/(2*n)

print("{0:.10f}".format(ans))