N = int(input())
A = []
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)

ALL = 1<<N

# cost[n][i]:訪れたことのある都市の集合n,最後にいる都市であるときのコスト最小値
cost = []
for i in range(ALL):
    c = [10**100]*N
    cost.append(c)

# 初期化
cost[0][0] = 0

# 集合nに要素iが含まれるかを判定してTrue/Falseを返す関数
def has_bit(n,i):
    return (n&(1<<i) >0)

for n in range(ALL):
    for i in range(N):  #出発点
        for j in range(N):   #到着点
            if has_bit(n,j) or j==i:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j] , cost[n][i] + A[i][j])

print(cost[ALL-1][0])