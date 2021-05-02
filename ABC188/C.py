N = int(input())
lisA = list(map(int,input().split()))

lmax = 0
rmax = 0
harfidx = 2**N//2
for i in range(harfidx):
    if lisA[i]>lmax:
        lmax = lisA[i]
        lidx = i
    if lisA[i+harfidx]>rmax:
        rmax = lisA[i+harfidx]
        ridx = i+harfidx

if lmax < rmax:
    ans = lidx + 1
else:
    ans = ridx + 1

print(ans)