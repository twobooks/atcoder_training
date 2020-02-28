# import math
# from fractions import gcd

import numpy as np
# import scipy as scp

# 入力の受け取り
a,b = map(int,input().split())

stra = str(a)*b
strb = str(b)*a

ans = min(stra,strb)

print(ans)