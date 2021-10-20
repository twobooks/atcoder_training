from heapq import heappush,heappop,heapify

N,M = list(map(int,input().split()))

# グラフを隣接リストで受け取る
G = [[] for _ in range(N)]
for _ in range(M):
    ui,vi,ci = list(map(int,input().split()))
    # 頂点番号は-1してゼロインデックスにする
    # ui -= 1
    # vi -= 1
    
    # uiとviの間に重みciの辺を張る
    G[ui].append((vi,ci))
    # G[vi].append((ui,ci)) # 無向グラフなら両方の頂点に辺を張る

################################################
# Dijkstra
# 計算量はO((N+M)*logM) Nは頂点の数、Mは辺の数
################################################

# 頂点0から各頂点への最短距離を保持する配列
dist = [-1 for _ in range(N)]
# done[i]:ヒープから頂点iを取り出したことがあるかを記憶する配列。Falseで初期化
done = [False for _ in range(N)]

# キューを用意して始点(距離,頂点番号)を追加
Q = []
heappush(Q,(0,0))

dist[0] = 0

while len(Q)>0:
    d,i = heappop(Q)

    # 前にヒープから取り出した頂点なら、隣接頂点を調べる前にスキップ
    if done[i] == True:
        continue

    # ヒープから頂点iを取り出したことを記録しておく
    done[i] = True

    # 頂点iに隣接する頂点を順番に見る。見ている頂点はjとする
    for (j,c) in G[i]:
        # 辺の重み
        x = c
        # jが未訪問のとき又はjへの最短距離が更新可能なとき、
        # jへの最短距離を更新してヒープの末尾にj(距離,頂点番号)を追加
        if dist[j]==-1 or dist[j]>dist[i]+x:
            dist[j] = dist[i] + x
            heappush(Q,(dist[j],j))

print(dist[N-1])