def main():
    # 高速化のため関数定義してその中で解を得る
    # グローバル関数へのアクセスは遅いらしい

    S = input()

    # 2**MAXまでダブリングする
    MAX = 20

    N = len(S)
    # ダブリング後の結果を格納する配列(next)
    # next[p][i] には 元々iにいた子が2**p回移動した後にいるマス目(0~i-1)が入る
    next = [[0] * N for _ in range(MAX)]

    # nextの初期化
    for i in range(N):
        if S[i] == "L":
            next[0][i] = i - 1
        else:
            next[0][i] = i + 1

    # ダブリング。pステップ後のnext[p][i]から更にpステップ後の状態next[p+1][i]は
    # next[p][next[p][i]]となる
    for d in range(MAX-1):
        for i in range(N):
            next[d+1][i] = next[d][next[d][i]]

    # 解を得るための下準備として配列resを準備
    res = [0] * N
    K = N*2
    for v in range(N):
        nv = v
        for d in range(MAX):
            if (K & (1 << d)):
                nv = next[d][nv]
        res[nv] += 1

    #　回答出力
    print(*res, sep=" ")


# main関数実行
main()
