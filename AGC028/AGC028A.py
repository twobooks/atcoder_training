from fractions import gcd

N,M = map(int,input().split())
S = input()
T = input()

G = gcd(N, M)
L = N * M // G
ng = N//G
mg = M//G

for i in range(G):
    Nnum = i*ng
    Mnum = i*mg
    if S[Nnum] != T[Mnum]:
        print(-1)
        exit()

print(L)
