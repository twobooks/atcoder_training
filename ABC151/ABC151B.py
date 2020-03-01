# import math
# from fractions import gcd

import numpy as np
# import scipy as scp

# 入力の受け取り
n,k,m = map(int,input().split())
arrA = np.array(input().split(),dtype=np.int64)

goal_score = m * n 
now_score = sum(arrA)

if (goal_score - now_score) > k:
    ans = -1
else:
    ans = max((goal_score -now_score),0)

print(ans)