import heapq

N,M = list(map(int,input().split()))

# グラフ(隣接リスト,無向グラフ)
G = [[] for _ in range(N)]
for _ in range(M):
    ui,vi,ci = list(map(int,input().split()))
    # 頂点番号は-1してゼロインデックスにする
    # ui -= 1
    # vi -= 1
    
    # uiとviの間に重みciの辺を張る
    G[ui].append((vi,ci))
    G[vi].append((ui,ci)) # 無向グラフなら両方の頂点に辺を張る

######################################
# Prim's algorithm(プリム法)
# グラフ理論で重み付き連結グラフの最小全域木を求める最適化問題のアルゴリズム
# 全域木のうち、その辺群の重みの総和が最小となる木を求めるものである
# 計算量は((N+M)logM).Nは頂点数、Mは辺数
######################################

# marked_count:マークされている頂点数を記憶する変数。初期値は0。Nになったら終了する
marked_count = 0

# marked[i]:頂点iがマークされているかを記憶する配列。初期値は全てFalse。マークされたらTrue
marked = [False for _ in range(N)]

# Q:ヒープキュー.最少のコストの辺を選ぶために使う
Q = []

# 初期化:最初に頂点0を選ぶ。アルゴリズム的にはどれを選んでも良いがforを回す便宜上0が無難
marked[0] = True
marked_count += 1
# ヒープQに頂点0に隣接する辺を入れる。
# その際、最少の辺を取り出せるように(コスト、頂点番号)の形で入れる
for j,c in G[0]:
    heapq.heappush(Q,(c,j))

# 最小全域木の重みを記憶する変数
ans = 0

while marked_count < N:
    # ヒープから最小コストの辺を取り出す
    c,i = heapq.heappop(Q)

    # iがマーク済みであれば処理をスキップ
    if marked[i]==True:
        continue

    # 頂点iをマークしてマーク済みカウントを増やす
    marked[i] = True
    marked_count += 1

    # 最小全域木の重みを更新
    ans += c

    # 新たにマークした頂点iに隣接した辺を調べる
    for j,c in G[i]:
        # 辺の先の頂点がマーク済みであればスキップ
        if marked[j]:
            continue
        heapq.heappush(Q,(c,j))

print(ans)
