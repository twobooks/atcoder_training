H,W = list(map(int,input().split()))

Anums = [[] for _ in range(H)]
yokoSum = [0 for _ in range(H)]
tateSum = [0 for _ in range(W)]
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(W):
        Anums[i].append(A[j])
        yokoSum[i] += A[j]
        tateSum[j] += A[j]

for i in range(H):
    for j in range(W):
        print(yokoSum[i]+tateSum[j]-Anums[i][j],end=" ")
    print()
