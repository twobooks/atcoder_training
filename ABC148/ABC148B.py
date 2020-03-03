# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
s,t = input().split()

ans = ""
for x in range(n):
    ans = ans + s[x]
    ans = ans + t[x]

print(ans)