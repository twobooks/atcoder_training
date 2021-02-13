N = int(input())
h = list(map(int,input().split()))
INF = float("INF")

# dpの用意（最小化を求めるならINFで初期化）
dp = [INF]*(N)
# 初期条件を設定（ベースケースの設定みたいな感じ）
dp[0] = 0

# 緩和処理の関数
def chmin(dp,i,j):
  if dp[i]>j:
    dp[i] = j

# 動的計画法の実行
for i in range(0,N):
  if i+1<N:
    chmin(dp,i+1,dp[i]+abs(h[i]-h[i+1]))
  if i+2<N:
    chmin(dp,i+2,dp[i]+abs(h[i]-h[i+2]))

# print(dp)
print(dp[N-1])
