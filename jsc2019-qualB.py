def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10**9+7
    sum1 = 0
    sum2 = 0
    for i in range(N):
        for j in range(N):
            if i < j and A[j] < A[i]:
                sum1 += 1
            if A[j] < A[i]:
                sum2 += 1
    ans = 0
    ans += (sum1 % mod) * K
    ans += sum2 * K * (K - 1) // 2
    ans %= mod
    print(ans)


solve()
