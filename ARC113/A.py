from math import ceil
K = int(input())

ans = 0
for a in range(1,K+1):
    for b in range(1,ceil(K/a)+1):
        ans += K//(a*b)

print(ans)