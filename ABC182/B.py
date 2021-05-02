N = int(input())
lisA = list(map(int,input().split()))

ans = lisA[0]
maxGCD = 0
for i in range(2,1001):
    tmp = 0
    for a in lisA:
        if a%i == 0:
            tmp += 1
    if tmp > maxGCD:
        ans = i
        maxGCD = tmp

print(ans)