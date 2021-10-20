N = int(input())
MOD = 10**9 + 7

# べき乗.計算量はO(logN)
Bekijou = pow(3,N,MOD)
print(Bekijou)

# 階乗
fact = [1]*(N+1)
for i in range(1,N+1):
    fact[i] = i * fact[i-1] % MOD
print(fact[N])

# 2項係数(nCk)
C = [[0]*(N+1) for _ in range(N+1)]
C[0][0] = 1
for i in range(1,N+1):
    C[i][0] = 1
    for j in range(1,i+1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]
# C[N][K]がnCkになる