N,B,K = list(map(int,input().split()))
C = list(map(int,input().split()))
MOD = 10**9 +7

############################
# 桁DP                     #
############################
# DP表を用意。DP[上から何桁目か(N)][Kで割った余り(K)]=組合せ数
DP = [[0]*B for _ in range(N+1)]
for k in range(K):
    DP[1][C[k] % B] += 1
# DP遷移
# DP[i+1][DP[(10j+k) mod B]]
for i in range(1,N+1):
    for j in range(B):
        for k in range(K):
            if i>N-1:
                break
            DP[i+1][(10*j + C[k]) % B] += DP[i][j]
            DP[i+1][(10*j + C[k]) % B] %= MOD
# DP[N][0]が答えなので出力
print(DP[N][0])