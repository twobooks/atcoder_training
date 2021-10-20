from bisect import bisect_left,bisect_right

N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

# bisect_rightはAi>Kとなるような最小のindexを返す。Kが複数あったら右に値を挿入できる感じ
# bisect_leftはAi>=Kとなるような最小のindexを返す。Kが複数あったら左に値を挿入できる感じ
# Trueとなるものが無ければlen(A)が返ってくる
ok = bisect_left(A,K)

if ok ==N:
    print(-1)
else:
    print(ok)