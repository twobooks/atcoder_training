# 動的計画法
N,L = list(map(int,input().split()))
X = list(map(int,input().split()))
T1,T2,T3 = list(map(int,input().split()))

# ハードルがある座標でTrueになる配列
H = [False]*(L+1)
for x in X:
    H[x] = True

# cost[i]:最少所要時間。大きい値を入れておいてminで更新していく
cost = [10**100]*(L+1)

cost[0] = 0

for i in range(1,L+1):
    # 行動1
    cost[i] = min(cost[i],cost[i-1]+T1)
    # 行動2
    if i >= 2:
        cost[i] = min(cost[i],cost[i-2]+T1+T2)
    # 行動3
    if i >= 4:
        cost[i] = min(cost[i],cost[i-4]+T1+3*T2)
    # ハードルがあれば加算
    if H[i]:
        cost[i] += T3

ans = cost[L]
for i in [L-3,L-2,L-1]:
    if i >= 0:
        ans = min(ans,cost[i] + T1//2 + T2*(2*L-2*i-1)//2)

print(ans)