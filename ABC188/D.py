import numpy as np

N,C = map(int,input().split())

daynums = []

for i in range(N):
    ai,bi,ci = map(int,input().split())
    daynums.append((ai,ci))
    daynums.append((bi+1,-ci))

daynums.sort()

fee = 0
d = 0
ans = 0
for day,num in daynums:
    if not(day == d):
        ans += (day - d) * min(fee,C)
        d = day
    fee += num

print(ans)
