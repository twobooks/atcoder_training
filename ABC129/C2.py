N,M = list(map(int,input().split()))

# ok[i]:i段目が使えるかを記録する配列
ok = [True] * (N+1)
for i in range(M):
    a = int(input())
    ok[a]=False

MOD = 10**9+7

# cnt[i]:i段目まで辿り着く移動方法の数
cnt = [0]*(N+1)

# 初期化。cnt[0]を1にする。直感と異なるが0!や0C0が1と定義するのと同じ発想かも
cnt[0] = 1

# 貰うDP.0は初期化済みなので1からNまでループ
for i in range(1,N+1):
    if ok[i]:
        # 本問題ではcntは1となる
        if cnt == 1:
            cnt[i] = 1
        else:
            cnt[i] = (cnt[i-1]+cnt[i-2]) % MOD
    else:
        # ok[i]がFalse、すなわち階段が壊れているなら辿り着けないのでcnt[i]は初期値0のまま
        continue

print(cnt[N])