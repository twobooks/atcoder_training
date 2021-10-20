import numpy as np    # np.lcm(),np.gcd()
from numba import njit, b1, i1, i4, i8, f8


@njit((i8, i8[:], i8[:]), cache=True)
def main(N, A, B):
    MOD = 998244353
    dp = [[0] * 3001 for i in range(3001)]
    for i in range(3001):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(0, 3001):
            if A[i-1] <= j <= B[i-1]:
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
                dp[j][i] %= MOD
            else:
                dp[j][i] = dp[j-1][i]
                dp[j][i] %= MOD
    # for i in range(4):
    #     lis = dp[i]
    #     print(lis[:N+1])
    print(dp[3000][N])


N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
main(N, A, B)
