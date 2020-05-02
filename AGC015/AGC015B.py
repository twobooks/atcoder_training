S = input()
N = len(S)

ans = 0
for i in range(0,N):
    if i == 0:
        ans += N-1
    elif i == N-1:
        ans += N-1
    elif S[i] == "U":
        ans += i*2
        ans += N-1-i
    elif S[i] == "D":
        ans += i
        ans += (N-1-i)*2

print(ans)
    