N,M = map(int,input().split())

lisN = [0] + [1]*N
ansSet = set([1])

for _ in range(M):
    # print(ansSet,lisN)
    x,y = map(int,input().split())
    if x in ansSet:
        ansSet.add(y)
    lisN[x] -= 1
    lisN[y] += 1
    if lisN[x] == 0:
        ansSet.discard(x)

print(len(ansSet))
