n,r = map(int,input().split())

if n >= 10:
    innerR = r
else:
    innerR = r + (100*(10-n))

print(innerR)