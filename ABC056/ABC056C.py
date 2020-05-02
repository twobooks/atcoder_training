X = int(input())

ans = 0
num = 1
tmp = 0
while tmp<X:
    tmp += num
    num += 1
    ans += 1

print(ans)