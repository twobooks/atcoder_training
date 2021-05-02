N = int(input())
lisP = list(map(int,input().split()))

setAll = set(range(200000+1))

for p in lisP:
    setAll = setAll.difference({p})
    print(min(setAll))
