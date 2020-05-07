N = int(input())
lisA = [1] + list(map(int,input().split()))

ans = 0
flg = False
for i,v in enumerate(lisA):
    if flg:
        flg = False
        continue
    elif i == v:
        ans += 1
        flg = True

print(ans)