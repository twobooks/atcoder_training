from fractions import gcd

N = int(input())
lisA = list(map(int,input().split()))

lisA.sort()
ans = 10**9 + 1

for num in lisA[1:]:
    tmp = gcd(lisA[0],num)
    ans = min(ans,tmp)
    if ans == 1:
        print(ans)
        exit()

print(ans)