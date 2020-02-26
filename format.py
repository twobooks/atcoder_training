import math

import numpy as np
import scipy as scp

# 入力の受け取り
n = int(input())
n,k = map(int,input().split())
# 配列入力の受け取り
arrA = np.array(input().split(),dtype=np.int64)
# 列ベクトルとかの受け取り
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())  # S += [input()] とも書ける
    # 整数として取り込むときは、 input() を int(input()) に置き換える。

print(ans)