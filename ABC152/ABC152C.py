# import math
# from fractions import gcd

import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
arrP = np.array(input().split(),dtype=np.int64)

minnum = arrP[0]

def func152C(arr,minnum):
    ans = 0
    for i in arr:
        if i <= minnum:
            minnum = i
            ans += 1
        else:
            continue
    return  ans

ans = func152C(arrP,minnum)
print(ans)