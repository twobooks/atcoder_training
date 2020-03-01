# import math
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
k,x = map(int,input().split())

if k * 500 >= x:
    ans = "Yes"
else:
    ans = "No"

print(ans)