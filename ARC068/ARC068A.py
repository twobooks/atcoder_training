X = int(input())

div11 , mod = divmod(X,11)
div6, mod = divmod(mod,6)
num = 1 if mod > 0 else 0
ans = div11 * 2 + div6 + num

print(ans)