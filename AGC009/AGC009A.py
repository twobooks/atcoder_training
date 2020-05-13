N = int(input())
lisAB = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for A,B in lisAB[::-1]:
    if (A+ans)%B == 0:
        continue
    else:
        num = B - (A+ans)%B
        ans += num

print(ans) 