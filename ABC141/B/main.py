# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
s = input()

ans = "Yes"
for i in range(1,len(s)+1):
    if i%2 == 1:
        if s[i-1] == "L":
            ans = "No"
            break
    if i%2 == 0:
        if s[i-1] == "R":
            ans = "No"
            break

print(ans)