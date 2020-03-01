# import math
from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
arrP = tuple(map(int, input().split()))
arrQ = tuple(map(int, input().split()))

perms_list = list(permus(range(1,n+1)))
a = perms_list.index(arrP)
b = perms_list.index(arrQ)

ans = abs(a-b)
# y = abs(a-b)
print(ans)