N = int(input())

# X[d]:d日目から実行可能になるタスクのポイントを集めた配列
X = [[] for _ in range(N)]
for i in range(N):
    Ai,Bi = list(map(int,input().split()))
    X[Ai-1].append(Bi)

# cnt[p]:ポイント数をキーとして現在日におけるポイントごとのタスクの個数を記録する配列
cnt = [0]*101
ans = 0
for d in range(N):
    for p in X[d]:
        cnt[p] += 1
    for p in range(100,0,-1):
        if cnt[p]>0:
            ans += p
            cnt[p] -= 1
            break
    print(ans)