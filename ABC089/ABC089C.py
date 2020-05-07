from collections import deque,Counter
from itertools import permutations,combinations,combinations_with_replacement

N = int(input())
rows = [input()[0] for _ in range(N)]

cnt = Counter(rows)

ans = 0
for k in combinations(["M","A","R","C","H"],3):
    ans += cnt[k[0]]*cnt[k[1]]*cnt[k[2]]

print(ans)
