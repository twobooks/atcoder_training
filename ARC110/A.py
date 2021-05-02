from scipy.special import comb,perm #permはnPk
import numpy as np

N = int(input())
arr1 = np.arange(2,N+1)
arr2 = arr1.copy()

ans = 1
for i in range(0,N-1):
    num = arr2[i]
    ans *= num
    mask = arr2 % num == 0
    arr2[mask] //= num

print(ans + 1)

