import math
from fractions import gcd

import numpy as np
import scipy as scp

# 入力の受け取り
n,k = map(int,input().split())
arrH = np.array(input().split(),dtype=np.int64)

arrH.sort()

ans = sum(arrH[::-1][k:])

print(ans)