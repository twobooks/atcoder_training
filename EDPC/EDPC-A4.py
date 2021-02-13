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

# メモ化再帰
def rec(dp,num):
  if dp[num]<INF: return dp[num]
  if num>0:
    chmin(dp,num,rec(dp,num-1)+abs(h[num]-h[num-1]))
  if num>1:
    chmin(dp,num,rec(dp,num-2)+abs(h[num]-h[num-2]))
  return dp[num]

# print(dp)
print(rec(dp,N-1))
