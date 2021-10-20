from collections import deque

N,M = list(map(int,input().split()))

# グラフを隣接リストで受け取る
G = [[] for _ in range(N)]
for _ in range(M):
    ai,bi = list(map(int,input().split()))
    # 頂点番号は-1してゼロインデックスにする
    ai -= 1
    bi -= 1
    # aiとbiの間に辺を張る
    G[ai].append(bi)
    G[bi].append(ai)

# BFS
# 頂点0から各頂点への最短距離を保持する配列
dist = [-1 for _ in range(N)]

# キューを用意して始点を追加
Q = deque()
Q.append(0)

dist[0] = 0

while len(Q)>0:
    i = Q.popleft()

    # 頂点iに隣接する頂点を順番に見る。見ている頂点はjとする
    for j in G[i]:
        # jが未訪問だったらjへの最短距離を更新してキューの末尾にjを追加
        if dist[j] == -1:
            dist[j] = dist[i]+1
            Q.append(j)

if dist[N-1] ==2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")



