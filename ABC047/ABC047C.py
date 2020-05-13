S = input()

tmp = S[0]
ans = 0
for s in S[1:]:
    if tmp != s:
        ans += 1
    tmp = s

print(ans)