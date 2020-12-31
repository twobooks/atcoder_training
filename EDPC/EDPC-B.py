import numba
import numpy as np

N,K = map(int,input().split())
h = list(map(int,input().split()))

@numba.njit
def main(N,K,h):
    dp = [np.inf for i in range(N+1)]
    dp[0] = 0

    dp[1] = abs(h[1]-h[0])
    if N==2:
        # print(dp[1])
        return dp

    for i in range(2,N):
        for j in range(1,K+1):
            if i-j>=0:
                dp[i] = min(dp[i],dp[i-j] + abs(h[i]-h[i-j]))
    return dp

# print(dp)
print(int(main(N,K,h)[N-1]))