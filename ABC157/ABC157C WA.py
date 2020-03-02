# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
n,m = map(int,input().split())

numlist = [" "]*n
muri = 0

for _ in range(m):
    s,c = map(int,input().split())
    if numlist[s-1] == " " or numlist[s-1] == c:
        numlist[s-1] = c
    else:
        muri = 1
        break

numlist = [0 if num == " " else num for num in numlist]
ans = int("".join(map(str,numlist)))

if muri == 1 or n != len(str(ans)):
    ans = -1

print(ans)