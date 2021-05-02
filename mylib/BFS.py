# 幅優先探索
from collections import deque

R,C = list(map(int,input().split()))
sy,sx = list(map(int,input().split()))
gy,gx = list(map(int,input().split()))
S = []
for i in range(R):
    s = input()
    S.append(s)

sy -= 1
sx -= 1
gy -= 1
gx -= 1

#始点からの最小移動回数を管理する2次元配列。
#-1が未訪問を表しVisitedを兼ねる
dist = []
for i in range(R):
    dist.append([-1]*C)

Q = deque()
Q.append([sy,sx])
dist[sy][sx] = 0

while len(Q)>0:
    i,j = Q.popleft()
    for i2,j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not (0<=i2<R and 0<=j2<C):
            continue
        if S[i2][j2] == "#":
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j]+1
            Q.append([i2,j2])

print(dist[gy][gx])
# print(dist[0][1])

