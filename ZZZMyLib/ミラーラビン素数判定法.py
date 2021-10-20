import sys
def input(): return sys.stdin.readline().rstrip()


# ミラーラビン素数判定法
# 素数ならTrue,非素数ならFalseを返す
def Miller_Rabin(N):

    # 1は非素数
    if N == 1:
        return False

    # 2は素数その他2の倍数は合成数
    if N % 2 == 0:
        if N == 2:
            return True
        else:
            return False

    # 偶数は篩落としたのでNは奇数でありN-1は偶数となる
    # ここでN-1を2^s*dと表すこととする
    temp = N-1
    s = 0
    while temp % 2 == 0:
        temp //= 2
        s += 1
    d = (N-1)//(2**s)

    # 比較対象リスト
    # 2^32未満なら2,7,61
    # 2^64未満なら37までの素数を使う
    # それ以上は2以上N未満の乱数50個を使う

    if N < 2**32:
        complist = (2, 7, 61)
    elif N < 2**64:
        complist = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    else:
        from random import randint
        complist = set()
        while len(complist) < 50:
            complist.add(randint(2, N-1))

    # aをcomplist中の数字でそれぞれ試してみる
    for a in complist:
        if N <= a:
            break

        # (a^d)%N=1ならこのaについてはミラーラビンテスト合格
        if pow(a, d, N) == 1:
            continue

        # 0<=r<sを満たす(a^(d*(2^r)))%Nを見ていき
        # -1≡N-1を満たすものが1つでもあればこのaについてミラーラビンテスト合格
        # 1つもなければその時点で不合格(非素数)
        for r in range(s):
            temp = pow(a, d*(2**r), N)
            if temp == N-1:
                break
        else:
            return False

    # すべてのaについてミラーラビンテストが合格したならおそらく素数と判定できる
    return True


N = int(input())
A = list(map(int, input().split()))

for a in A:
    if Miller_Rabin(a):
        print("Yes")
    else:
        print("No")
