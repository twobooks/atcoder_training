from fractions import gcd

N = int(input())
rows = [int(input()) for _ in range(N)]

def lcm(x, y):
    return (x * y) // gcd(x, y)

ans = 1
for num in rows:
    ans = lcm(ans,num)

print(ans)