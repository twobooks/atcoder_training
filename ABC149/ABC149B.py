# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
a,b,k = map(int,input().split())

takahasi = a
aoki = b

if k >= takahasi:
    k = k - takahasi
    takahasi = 0
else:
    takahasi -= k
    k = 0

if k >= aoki:
    aoki = 0
else:
    aoki -= k

print(takahasi,aoki)