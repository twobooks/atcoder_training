N,K = map(int,input().split())

def func(num):
    g2 = int("".join(sorted(str(num))))
    g1 = int("".join(sorted(str(num))[::-1]))
    return g1-g2

for k in range(K):
    N = func(N)

print(N)