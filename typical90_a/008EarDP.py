N = int(input())
S = input()
MOD = 10**9 + 7

atcoder = "atcoder"

dp = [[0]*(len(S)+1) for i in range(8)]

dp[0][0] = 1

for i in range(8):
    for j in range(len(S)):
        # if j < len(S):
        dp[i][j+1] += dp[i][j]
            # dp[i][j+1] %= MOD
        if i < 7 and atcoder[i] == S[j]:
            dp[i+1][j+1] += dp[i][j]
            # dp[i+1][j+1] %= MOD

ans = dp[7][len(S)] % MOD
print(ans)
