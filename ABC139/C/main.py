# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
# 配列入力の受け取り
arrH = list(map(int,input().split()))

i = 0
temp = 0
ans = 0
while i < n:
    if i == n-1:
        ans = max(ans,temp)
        break
    elif arrH[i] >= arrH[i+1]:
        temp += 1
        i += 1
    else:
        ans = max(ans,temp)
        temp = 0
        i +=1

print(ans)
# print("{:.10f}".format(ans))
