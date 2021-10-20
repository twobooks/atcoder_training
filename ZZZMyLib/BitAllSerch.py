N = int(input())
A = []
for i in range(N-1):
    # A[i]はA[i][i+1]から始まるため0~iまでのi+1個はダミーで埋める
    lst = list(map(int,input().split()))
    A.append([0]*(i+1)+lst)

ALL = 1<<N

happy = [0]*ALL

# nで表現される集合に要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n,i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(N):
        for j in range(i+1,N):
            if has_bit(n,i) and has_bit(n,j):
                happy[n] += A[i][j]

ans = -10**100

# 1つ目の集合
for n1 in range(ALL):
    # 2つ目の集合
    for n2 in range(ALL):
        # n1とn2で重複があれば無視する
        if n1&n2 >0:
            continue
        # n1とn2の補集合。全体集合ALL-1からn1,n2の和集合を引く
        n3 = ALL-1 -(n1|n2)
        ans = max(ans,happy[n1]+happy[n2]+happy[n3])

print(ans)