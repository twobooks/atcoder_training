N = int(input())

ans = -(10**9+1)
for i in range(N):
    if i == 0:
        minnum = int(input())
        continue
    num = int(input())
    ans = max(ans,num-minnum)
    minnum = min(minnum,num)

print(ans)