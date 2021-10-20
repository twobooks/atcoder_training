INF = 1_000_000_000_000_000_000

N,M = list(map(int,input().split()))

# dist[u][v]:全ての頂点の組についての最短距離を保存する2次元配列
dist = [[INF]*N for _ in range(N)]

# グラフの辺を受け取りdistに直接書き込む
for _ in range(M):
    u,v,c = list(map(int,input().split()))
    dist[u][v] = c
 
# 初期化:dist[i][i]は0にする
for i in range(N):
    dist[i][i] = 0

####################################
# Warshall–Floyd Algorithm
# 計算量はO(N**3)
# 概ね全点ダイクストラ法より速い
####################################

for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y],dist[x][k]+dist[k][y])

ans = 0
for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)