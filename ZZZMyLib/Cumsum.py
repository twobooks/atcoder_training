N = int(input())
S = input()

# 向きを変える必要がある人数の最小値を保持する変数
# 大きい値で初期化しておく
min_turn = 10**100

# "W"の数の累積和
# 0番目は0が返るように0を頭に入れる
sum_W = [0]
for i in range(0,N):
    if S[i] == "W":
        sum_W.append(sum_W[i]+1)
    else:
        sum_W.append(sum_W[i])

for i in range(0,N):
    # リーダーより左にいて左（W)を向いている人の数W
    W = sum_W[i]
    # リーダーより右に居て右(E)を向いている人の数E
    E = (N-i-1) - (sum_W[N]-sum_W[i+1])

    turn = W+E

    min_turn = min(min_turn,turn)

print(min_turn)
