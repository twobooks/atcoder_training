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

for j in range((i + 1) % N, (i + 1) % N + N):
    if j % N == i:
        break
    tmp = (j-1) % N
    ans[j % N] = min(T[j % N], ans[tmp]+S[tmp], ans[j % N])

print(*ans, sep="\n")
