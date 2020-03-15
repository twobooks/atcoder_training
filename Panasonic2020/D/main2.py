# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter

# import numpy as np
# import scipy as scp

# 入力の受け取り
n = int(input())

strlist = "abcdefghij"

def dfs(s,num):
    if len(s) >= n:
        print(s)
        return
    elif num ==0:
        dfs("a",1)
    else:
        for i in range(num):
            dfs(s+strlist[i],num)
        dfs(s+strlist[num],num+1)

dfs("",0)