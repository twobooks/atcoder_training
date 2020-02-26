import math

import numpy as np
import scipy as scp

# 入力の受け取り
s,t = input().split()
a,b = map(int,input().split())
u = input()

dic = {s:a,t:b}

if u == s:
    dic[s] -= 1
else:
    dic[t] -= 1

print(dic[s],dic[t])