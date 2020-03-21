# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import scipy as scp

# 入力の受け取り
n,k,q = map(int,input().split())
correct_member = [int(input())-1 for _ in range(q)]

ans = [k-q for _ in range(n)]

cormem_count = Counter(correct_member)

for k,v in cormem_count.items():
    ans[k] += v

for i in ans:
    YorN = "Yes" if i > 0 else "No"
    print(YorN)
