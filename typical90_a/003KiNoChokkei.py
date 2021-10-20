from collections import deque

N = int(input())

G = [[] for i in range(N+1)]
for i in range(1,N):
    A,B = list(map(int,input().split()))
    G[A].append(B)
    G[B].append(A)

#始点からの最小移動回数を管理する2次元配列。
#-1が未訪問を表しVisitedを兼ねる
dist = []
for i in range(N+1):
    dist.append(-1)

Q = deque()
Q.append(1)
dist[1] = 0

while len(Q)>0:
    i = Q.popleft()
    for i2 in G[i]:
        if dist[i2] == -1:
            dist[i2] = dist[i]+1
            Q.append(i2)

# distでmaxdistのindexを取得して1からどこが一番遠いか調べる
town,maxdist = -1,-1
for i in range(N+1):
    if dist[i]>maxdist:
        maxdist = dist[i]
        town = i

# 上記の一番遠い町からもう一回DFSする
dist = []
for i in range(N+1):
    dist.append(-1)

Q = deque()
Q.append(town)
dist[town] = 0

while len(Q)>0:
    i = Q.popleft()
    for i2 in G[i]:
        if dist[i2] == -1:
            dist[i2] = dist[i]+1
            Q.append(i2)

# dist2のmaxdistとって+1したのがans
# print(dist)
ans = max(dist)
print(ans+1)