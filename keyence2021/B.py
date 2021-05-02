from collections import deque,Counter

N,K = map(int,input().split())
cntA = Counter(map(int,input().split()))

hako = K
ans = 0
for i in range(N):
    if cntA[i]==0:
        print(ans)
        exit()
    ans += min(cntA[i],hako)
    hako = min(hako,cntA[i])

print(ans)