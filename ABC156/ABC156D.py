n,a,b = map(int,input().split())

mod = 10**9 + 7

def comb(n:int,k:int,MOD:int):
    """return nCk (mod MOD)
    """
    nCk = 1
    # n!/(n-k)!
    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD
    # 1/k!
    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

all = pow(2,n,mod)-1
comb_a = comb(n,a,mod)
comb_b = comb(n,b,mod)
answer = (all -comb_a -comb_b) % mod

print(answer)