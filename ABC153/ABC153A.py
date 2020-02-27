import math
from fractions import gcd

import numpy as np
import scipy as scp

# 入力の受け取り
h,a = map(int,input().split())

ans = 0
while h > 0:
    h -= a
    ans += 1

print(ans)