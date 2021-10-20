N = int(input())
ps = [0] + list(map(int,input().split()))

P = sum(ps)

exist = []
for i in range(N+1):
    exist.append([False]*(P+1))

# 初期化
exist[0][0] = True

for i in range(1,N+1):
    for s in range(P+1):
        if exist[i-1][s]:
            exist[i][s] = True
        if s-ps[i]>=0 and exist[i-1][s-ps[i]]:
            exist[i][s] = True

ans = 0
for s in range(P+1):
    if exist[N][s]:
        ans += 1
print(ans)