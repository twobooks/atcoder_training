# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
a,b = map(int,input().split())

ans = 0
concentnum = 1
while concentnum <b:
    concentnum = concentnum -1 +a
    ans += 1

# print(concentnum)
print(ans)
# print("{:.10f}".format(ans))
