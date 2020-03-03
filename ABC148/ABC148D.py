n = int(input())
arrA = list(map(int,input().split()))

ans = 0
target = 1

for x in range(n):
    if arrA[x] == target:
        target += 1
        continue
    else:
        ans +=1

if ans == n:
    ans = -1

print(ans)