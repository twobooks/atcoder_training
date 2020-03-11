# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
# from collections import Counter

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
s = input()

arrS = list(s)

ans = 1
for i in range(1,len(arrS)):
    if arrS[i-1] != arrS[i]:
        ans += 1
    else:
        continue

print(ans)