N = int(input())

ans = 0
flg = False
for i in range(N):
    D1,D2 = map(int,input().split())
    if D1 == D2:
        ans +=1
    else:
        ans = 0
    if ans >= 3:
        flg = True
        # exit()

if flg is True:
    print("Yes")
else:
    print("No")