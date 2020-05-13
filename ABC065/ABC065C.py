from math import factorial,sqrt,ceil #,gcd

N,M = map(int,input().split())
MOD = 10**9 + 7

if abs(N-M)>=2:
    print(0)
    exit()

if N==M:
    ans = factorial(N) % MOD
    ans = ans * factorial(M) % MOD
    ans = ans * 2 % MOD  
    print(ans)
    exit()
elif N>M:
    ans = factorial(N) % MOD * factorial(M) % MOD
    print(ans)
    exit()
elif M>N:
    ans = factorial(M) % MOD * factorial(N) % MOD
    print(ans)
    exit()