from collections import defaultdict

N,X = list(map(int,input().split()))

# N個の品物をA,Bに分ける。偶奇で分ける
A = []
B = []
for i in range(N):
    w = int(input())
    if i%2 == 0:
        A.append(w)
    else:
        B.append(w)

# Bit集合nの中にiが含まれるか判定してTrue/Falseを返す関数
def has_bit(n,i):
    return (n&(1<<i) > 0)

# グループBを全列挙して重さ合計をキーとして組合せ数を集計
dic = defaultdict(int)
for n in range(1<<len(B)):
    s = 0
    # for i in range(N):
    for i in range(len(B)):
        if has_bit(n,i):
            s += B[i]
    dic[s] += 1

# グループAを全列挙して答えを求める
ans = 0
for n in range(1<<len(A)):
    s = 0
    # for i in range(N):
    for i in range(len(A)):
        if has_bit(n,i):
            s += A[i]
    ans += dic[X-s]

print(ans)