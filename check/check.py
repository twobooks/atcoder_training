import math
import os

import numpy as np
import scipy as scp
import sklearn as skl

# 入力の受け取り
n = int(input())
n,k = map(int,input().split())

arr = np.array(input().split(),dtype=np.int64)

# 演算子
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算
a % b         # a を b で割った余り
a ** b        # a の b 乗
a // b        # 切り捨て除算

# コンソールのクリア
os.sysytem("cls")

# 組合せの計算
def comb(n:int,k:int,MOD:int):
    """return nCk (mod MOD)
    """
    nCk = 1
    # n!/(n-k)!
    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD
    # 1/k!
    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

# 繰返し二乗法
# pythonだと標準関数でOK
pow(n,p,mod) # n:底、p:指数、mod:mod

# 文字列の分割
import re
st = "???a?bb????ccc?"
re.split("[a-z]",st)    #正規表現で指定してsplitできる
max([len(i) for i in re.split("\?",st)])  #split後の文字数の最大値を求める




