N = int(input())
S = input()

# 案の定TLE
# ans = N+1
# for i in range(N):
#     ans = min(ans,S[:i].count("W") + S[i+1:].count("E"))

left = 0
right = S.count("E")
ans = N+1
for i in range(N):
    if S[i] == "E":
        right -= 1
    ans = min(ans,left + right)
    if S[i] == "W":
        left += 1

print(ans)
