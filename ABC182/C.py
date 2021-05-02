N = input()
K = len(N)

ans = K+1
S = ""
def solve(S,i):
    global ans
    if i >=K:
        if S == "":
            return
        if int(S) % 3 == 0:
            ans = min(ans,K-len(S))
            return
        return 
    solve(S+N[i],i+1)
    solve(S,i+1)

solve(S,0)
print(-1 if ans>K else ans)