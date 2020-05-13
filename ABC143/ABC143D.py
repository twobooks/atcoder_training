import bisect

N = int(input())
lisL = list(map(int,input().split()))

lisL.sort()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ab = lisL[i] + lisL[j]
        ans += bisect.bisect_left(lisL[j+1:],ab)

print(ans)