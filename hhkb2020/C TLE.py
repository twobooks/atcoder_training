import numpy as np    # np.lcm(),np.gcd()

N = int(input())
arrP = np.array(input().split(),dtype=np.int64)

arrAll = np.arange(200000+1,dtype=np.int64)
mask = np.ones(200000+1,dtype=np.int64) == 1

for p in arrP:
    mask[p] = False
    print(arrAll[mask][0])