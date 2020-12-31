import numpy as np
from numba import njit
  
# @njit
# @njit(cache = True)
@njit('(i4[::1],)', cache=True)
def solve(A):
    count = np.zeros(10**6 + 10, np.int32)
    for x in A:
        if count[x] > 1:
            continue
        count[::x] += 1
    ret = 0
    for x in A:
        ret += count[x] == 1
    return ret

N = int(input())
A = np.array(list(map(int,input().split())), np.int32)
 
print(solve(A))
