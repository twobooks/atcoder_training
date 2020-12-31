from collections import deque,Counter

N = int(input())
A = list(map(int,input().split()))

memo = [0] * (10**6+10)
cnt = Counter(A)
for k,v in cnt.items():
    if memo[k] > 1:
        continue
    for j in range(k,10**6+1,k):
        memo[j] += v 

# print(memo[:max(A)+1])

ans = 0
for num in cnt:
    ans += (memo[num] == 1)

print(ans)
