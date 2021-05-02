from math import factorial,sqrt,ceil #gcd

N = int(input())
lisA = list(map(int,input().split()))

mdis = 0
edis = 0
cdis = 0
for x in lisA:
    mdis += abs(x)
    edis += x**2
    cdis = max(cdis,abs(x))

print(mdis,sqrt(edis),cdis,sep="\n")