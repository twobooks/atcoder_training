N,X = map(int,input().split())
lisA = list(map(int,input().split()))

ans = []
for a in lisA:
    if a == X:
        continue
    ans.append(a)

print(*ans)