A,R,N = list(map(int,input().split()))

def solve(A,R,N):
    if R == 1:
        return A
    else:
        ans = A
        for _ in range(1,N):
            ans *= R
            if ans > 10**9:
                return "large"
        return ans

ans = solve(A,R,N)
print(ans)