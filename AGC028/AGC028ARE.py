from fractions import gcd

N,M = map(int,input().split())
S = input()
T = input()

Xlen = N * M // gcd(N, M)
X = [0] * Xlen

for i,s in enumerate(list(S)):
    num = i*(Xlen//N)
    X[num] = s

for i,t in enumerate(list(T)):
    num = i*(Xlen//M)
    if X[num] == 0 or X[num] == t:
        continue
    else:
        print(-1)
        exit()

print(Xlen)
