N,C,K = map(int,input().split())
lisT = [int(input()) for _ in range(N)]

lisT.sort()
teiin = C
limit = K
timeup = 0
passengers = C
buscnt = 0
for i in range(N):
    if lisT[i] > timeup or passengers==0:
        timeup = lisT[i] + K
        passengers = C
        buscnt += 1
        passengers -= 1
    else:
        passengers -= 1

print(buscnt)



