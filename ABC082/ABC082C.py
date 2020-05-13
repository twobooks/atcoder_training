from collections import deque,Counter

N = int(input())
lisA = list(map(int,input().split()))

cnt = Counter(lisA)

ans = 0
for k,v in cnt.items():
    if k == v:
        continue
    elif v > k:
        ans += v-k
    else:
        ans += v

print(ans)