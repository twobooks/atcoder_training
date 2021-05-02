from math import ceil
N = int(input())

ans = 0
sameans = 0
for a in range(1,ceil(N**0.5)):
    for b in range(a,N//a+1):
        # print(a,b,N-a*b)
        if a*b<N and a != b:
           ans += 1
        elif a*b<N and a == b:
            sameans += 1

print(ans*2 + sameans) 