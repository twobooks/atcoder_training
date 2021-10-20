N,M = list(map(int,input().split()))

# 1始まりにするのにダミー(0)を入れる
S = [0]
C = [0]
for i in range(M):
    s,c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == "Y":
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c)) 

ALL = 1<<N

# cost[i][n]:i番目の販売セットまで見てそろった部品の集合がnであるときのコストの最小値
cost = []
INF = 10**100
for i in range(M+1):
    cost.append([INF]*ALL)

# 初期条件
cost[0][0] = 0

for i in range(1,M+1):
    for n in range(ALL):
        # iのセットを買わない場合
        cost[i][n] = min(cost[i][n],cost[i-1][n])
        # iのセットを買う場合
        cost[i][n|S[i]] = min(cost[i][n|S[i]],cost[i-1][n]+C[i])

ans = cost[M][ALL-1]
if ans == INF:
    ans = -1

print(ans)