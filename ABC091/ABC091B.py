# import math
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque
from collections import Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())
arrN = []
for _ in range(n):
    arrN += [input()]  #table.append(input())とも書ける
m = int(input())
arrM = []
for _ in range(m):
    arrM += [input()]  #table.append(input())とも書ける

countaN = Counter(arrN)
countaM = Counter(arrM)
countaAns = countaN - countaM

if len(countaAns) !=0:
    s,ans = countaAns.most_common()[0]
else:
    ans = 0

print(ans)