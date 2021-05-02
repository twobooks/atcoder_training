from math import log2,factorial,sqrt,ceil #gcd

N = int(input())

for b in range(1,N+1):
    if N - 5**b < 0:
        break
    tmp = N - 5**b
    for a in range(1,N+1):
        if tmp - 3**a < 0:
            break
        if tmp == 3**a:
            print(a,b)
            exit()

print(-1)