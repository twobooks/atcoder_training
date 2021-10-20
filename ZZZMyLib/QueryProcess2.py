import sys
sys.setrecursionlimit(1000000)

N = int(input())

# 根(社長)の頂点番号を記憶する変数
R = -1

# edges[i]:頂点iの子(部下)の頂点番号たち
edges = [[] for _ in range(N)]

for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

# クエリを受け取りaの値で分類する
# queries[a]:aの値に対応する[クエリ番号,bの値]を並べた配列
queries = [[] for _ in range(N)]
Q = int(input())
for q in range(Q):
    a,b = list(map(int,input().split()))
    queries[a-1].append([q,b-1])

# 答えとなる配列。True/Falseで格納する
ans = [False]*Q
# boos[i]:頂点iが今見ている頂点の上司ならTrue
boss = [False]*N

def dfs(i):
    # クエリを処理する
    for q,b in queries[i]:
        ans[q] = boss[b]
    # 自身を上司に設定する
    boss[i] = True
    # 再帰で子を見ていく
    for j in edges[i]:
        dfs(j)
    # 抜けるときに自信を上司から外す
    boss[i] = False

dfs(R)

for q in range(Q):
    if ans[q]:
        print("Yes")
    else:
        print("No")