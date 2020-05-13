from collections import Counter

N = int(input())
S = input()
MOD = 10**9 + 7

cnt = Counter(S)

slist = "abcdefghijklmnopqrstuvwxyz"
ans = 1
for s in slist:
    ans *= cnt[s] + 1

ans -= 1

ans = ans % MOD

print(ans)