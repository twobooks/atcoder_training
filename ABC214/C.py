import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
Ttmp = []
for i in range(N):
    t = T[i]
    Ttmp.append([t, i])

Ttmp.sort()
# print(T, S)
INF = 10**16
ans = [INF] * N
t, i = Ttmp[0]
ans[i] = t
# print(ans)
# ans[i] = min(T[i],ans[(i-1)%N]+S[(i-1)%N])


def recursive(idx, N):
    # print(idx)
    if ans[idx] < INF:
        return ans[idx]
    tmp = (idx - 1) % N
    ans[idx] = min(T[idx], recursive(tmp, N) + S[tmp], ans[idx])
    return ans[idx]


recursive((i-1) % N, N)
print(*ans, sep="\n")
