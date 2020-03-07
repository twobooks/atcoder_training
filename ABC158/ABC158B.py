n,a,b = map(int,input().split())

div, mod = divmod(n,(a+b))

ans = div * a
if mod <=a:
    ans += mod
else:
    ans += a

print(ans)
