# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
n,k = map(int,input().split())

ans = k * (k-1)**(n-1)
print(ans)
# print("{:.10f}".format(ans))