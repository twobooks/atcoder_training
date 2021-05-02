N = int(input())
lisP = list(map(int,input().split()))

lisALL = [True for i in range(200001)]
ans = 0
for p in lisP:
    lisALL[p] = False
    if ans ==p:
        for i in range(ans,200001):
            if lisALL[i] is False:
                continue
            elif lisALL[i] is True:
                ans = i
                break
    print(ans)
