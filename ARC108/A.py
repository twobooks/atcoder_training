S,P = map(int,input().split())

ans = "No"
for i in range(1,P+1):
    if i > P**0.5:
        break
    N = i
    M = S-i
    if M < 1:
        continue
    if N*M == P:
        ans = "Yes"
        break

print(ans)