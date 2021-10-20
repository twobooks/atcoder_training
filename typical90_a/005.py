import numpy as np

N,B,K = list(map(int,input().split()))
C = list(map(int,input().split()))
MOD = 10**9 +7

###############################
### 行列累乗を使ったDP       ###      
###############################
# オーバーフローをうまく処理できない

def multiply(A, B, MOD):
	# A × B を求める
	return np.dot(A,B) % MOD

def powers(A, T, MOD):
	# A の T 乗を求める
    res = np.eye(A[0].size,dtype=np.int64)
    while T > 0:
        if (T & 1):
            res = multiply(res,A,MOD)  # T の最下位bitが 1 ならば x^(2^i) をかける
        A = multiply(A,A,MOD)
        T = (T>>1)  # T を1bit 左にずらす
    return res

# 行列Aを用意
A = np.zeros(B*B,dtype=np.int64).reshape(B,B)
for i in range(B):
	for j in range(K):
		nex = (i * 10 + C[j]) % B
		A[i][nex] += 1

# 行列AのN乗する
# Z = np.linalg.matrix_power(A, N)
Z = powers(A,N,MOD)

# MODで割る
# ans = Z % MOD
# DP[N][0]が答えなので出力
print(Z[0][0])