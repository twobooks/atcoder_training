# import math
# from itertools import permutations as permus
# from fractions import gcd

# import numpy as np
# import scipy as scp

# 入力の受け取り
n,m = map(int,input().split())

arrSC = []
for _ in range(m):
    arrSC.append(list(map(int,input().split()))) # 行列の場合
    
ans = -1

def Ncheck(strnum):
    if len(strnum) != n:
        return False
    return True

def SCcheck(strnum):
    for i in range(m):
        if strnum[arrSC[i][0]-1] != str(arrSC[i][1]):
            return False
    return True

for num in range(1000):
    strnum = str(num)
    if Ncheck(strnum) and SCcheck(strnum):
        ans = num
        break

print(ans)