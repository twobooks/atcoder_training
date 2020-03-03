from fractions import gcd

a,b = map(int,input().split())

def lcm(x:int, y:int)->int:
    """
    return Least common multiple (最小公倍数)
    """
    return (x * y) // gcd(x, y)

ans = lcm(a,b)

print(ans)