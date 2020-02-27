import math
from fractions import gcd

import numpy as np
import scipy as scp

# 入力の受け取り
h,n = map(int,input().split())
arrA = np.array(input().split(),dtype=np.int64)

atack = sum(arrA)
if atack>=h:
    ans = "Yes"
else:
    ans = "No"
# ans = "Yes" or "No"
print(ans)