import math

import numpy as np
import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrA = np.array(input().split(),dtype=np.int64)

setA = set(arrA)

if len(arrA)==len(setA):
    ans = "YES"
else:
    ans = "NO"

print(ans)