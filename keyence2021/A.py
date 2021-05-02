N = int(input())
lisA = list(map(int,input().split()))
lisB = list(map(int,input().split()))

amax = 0
bmax = 0
ans = [0]*N
ans[0] = lisA[0]*lisB[0]

for i in range(N):
    if i == 0:
        amax = max(amax,lisA[i])
        print(ans[i])
        continue
    amax = max(amax,lisA[i])
    tmp = amax * lisB[i]
    ans[i] = max(ans[i-1],tmp)
    print(ans[i])