N,Q = map(int,input().split())
S = input()

ansLis = [0]
tmp = 0
flgA = False
for i in range(N):
    if flgA and S[i]=="C":
        tmp += 1
    ansLis.append(tmp)
    flgA = (S[i] == "A")
# print(ansLis)

ans = []
for _ in range(Q):
    l,r = map(int,input().split())
    num = ansLis[r] - ansLis[l]
    # if S[l-2] == "A" and S[l-1] == "C":
    #     num = max(0, num-1)
    ans.append(num)

print(*ans,sep="\n")