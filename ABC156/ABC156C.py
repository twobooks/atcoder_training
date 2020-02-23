import numpy as np

n = int(input())
x = np.array(input().split(),dtype=np.int64)

shouhiHP = 1001001001000
for k in range(min(x),max(x)+1):
    xHP = x - k
    xHP2jou = xHP ** 2
    sum_xHP = sum(xHP2jou)
    if sum_xHP < shouhiHP:
        shouhiHP = sum_xHP
    else:
        pass

print(shouhiHP)