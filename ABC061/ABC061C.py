from collections import deque,Counter

N,K = map(int,input().split())
cnt = Counter()
for _ in range(N):
    A,B = map(int,input().split())
    cnt[A] += B

sortedKeys = sorted(list(cnt.keys()))

tmp = K
for k in sortedKeys:
    tmp -= cnt[k]
    if tmp <= 0:
        print(k)
        exit()
