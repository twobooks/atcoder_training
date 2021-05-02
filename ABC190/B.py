N,S,D = map(int,input().split())

ans = "No"
for n in range(N):
    X,Y = map(int,input().split())
    if X>=S or Y<=D:
        continue
    else:
        print("Yes")
        exit()
print(ans)