import numpy as np
from numba import njit

N,W = map(int,input().split())

weight = np.array([],dtype=np.int64)
value = np.array([],dtype=np.int64)
for i in range(N):
    w,v = map(int,input().split())
    weight = np.append(weight,w)
    value = np.append(value,v)

dp = np.zeros((N+1,W+1),dtype=np.int64)

# def chmax(i,w,b,dp):
#     # global dp
#     if dp[i][w] < b:
#         dp[i][w] = b

@njit
def solve(N,W,weight,value,dp):
    for i in range(N):
        for w in range(W+1):
            if w-weight[i]>=0:
                if dp[i+1][w] < dp[i][w-weight[i]]+value[i]:
                    dp[i+1][w] = dp[i][w-weight[i]]+value[i]
            if dp[i+1][w] < dp[i][w]:
                dp[i+1][w] = dp[i][w]
    return dp[N][W]

ans = solve(N,W,weight,value,dp)
print(ans)