T = int(input())

def solve(L,R):
    xmax = R-L
    if xmax<L:
        return 0
    X = xmax - L + 1
    ymax = 1 + (X-1)*1
    res = (ymax + 1) * X // 2
    return res

ans = []
for _ in range(T):
    L,R = map(int,input().split())
    ans.append(solve(L,R))

print(*ans,sep="\n")
